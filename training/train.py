
import os
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, random_split
from torch.optim import Adam

from config import Config
from src.segmentation import UNet
from training.dataset import SatelliteDataset


def train_model():

    # Select training device
    device = torch.device(
        "cuda" if torch.cuda.is_available()
        else "cpu"
    )

    print(f"Training device: {device}")

    # Dataset paths
    image_dir = os.path.join(
        Config.RAW_DATA_DIR,
        "images"
    )

    mask_dir = os.path.join(
        Config.RAW_DATA_DIR,
        "masks"
    )

    # Load dataset
    dataset = SatelliteDataset(
        image_dir=image_dir,
        mask_dir=mask_dir
    )

    if len(dataset) < 2:
        raise ValueError(
            "At least two labeled image samples "
            "are required for training."
        )

    # Split dataset
    train_size = int(len(dataset) * 0.8)
    validation_size = len(dataset) - train_size

    generator = torch.Generator().manual_seed(42)

    train_dataset, validation_dataset = random_split(
        dataset,
        [train_size, validation_size],
        generator=generator
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=Config.BATCH_SIZE,
        shuffle=True,
        num_workers=0
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=Config.BATCH_SIZE,
        shuffle=False,
        num_workers=0
    )

    # Initialize U-Net
    model = UNet().to(device)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()

    optimizer = Adam(
        model.parameters(),
        lr=Config.LEARNING_RATE
    )

    best_validation_loss = float("inf")

    os.makedirs(
        Config.CHECKPOINT_DIR,
        exist_ok=True
    )

    checkpoint_path = os.path.join(
        Config.CHECKPOINT_DIR,
        "best_unet.pth"
    )

    # Training loop
    for epoch in range(Config.EPOCHS):

        model.train()

        running_loss = 0.0

        for images, masks in train_loader:

            images = images.to(device)
            masks = masks.to(device)

            optimizer.zero_grad()

            predictions = model(images)

            loss = criterion(
                predictions,
                masks
            )

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

        train_loss = (
            running_loss / len(train_loader)
        )

        # Validation
        model.eval()

        validation_loss = 0.0

        with torch.no_grad():

            for images, masks in validation_loader:

                images = images.to(device)
                masks = masks.to(device)

                predictions = model(images)

                loss = criterion(
                    predictions,
                    masks
                )

                validation_loss += loss.item()

        validation_loss /= len(validation_loader)

        print(
            f"Epoch [{epoch + 1}/{Config.EPOCHS}] "
            f"Training Loss: {train_loss:.4f} "
            f"Validation Loss: {validation_loss:.4f}"
        )

        # Save best checkpoint
        if validation_loss < best_validation_loss:

            best_validation_loss = validation_loss

            torch.save(
                model.state_dict(),
                checkpoint_path
            )

            print("Best model checkpoint saved.")

    print("\nTraining completed!")

    print(
        f"Best validation loss: "
        f"{best_validation_loss:.4f}"
    )

    print(
        f"Model saved at: {checkpoint_path}"
    )


if __name__ == "__main__":
    train_model()
