
import torch
import torch.nn as nn

from config import Config


class DoubleConv(nn.Module):
    """
    Two convolution layers with batch normalization
    and ReLU activation.
    """

    def __init__(self, in_channels, out_channels):
        super().__init__()

        self.block = nn.Sequential(
            nn.Conv2d(
                in_channels,
                out_channels,
                kernel_size=3,
                padding=1,
                bias=False
            ),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),

            nn.Conv2d(
                out_channels,
                out_channels,
                kernel_size=3,
                padding=1,
                bias=False
            ),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.block(x)


class UNet(nn.Module):
    """
    U-Net architecture for satellite image
    semantic segmentation.
    """

    def __init__(
        self,
        in_channels=Config.IMAGE_CHANNELS,
        num_classes=Config.NUM_CLASSES
    ):
        super().__init__()

        # Encoder
        self.encoder1 = DoubleConv(in_channels, 64)
        self.encoder2 = DoubleConv(64, 128)
        self.encoder3 = DoubleConv(128, 256)
        self.encoder4 = DoubleConv(256, 512)

        self.pool = nn.MaxPool2d(2)

        # Bottleneck
        self.bottleneck = DoubleConv(512, 1024)

        # Decoder
        self.upconv4 = nn.ConvTranspose2d(
            1024, 512, kernel_size=2, stride=2
        )
        self.decoder4 = DoubleConv(1024, 512)

        self.upconv3 = nn.ConvTranspose2d(
            512, 256, kernel_size=2, stride=2
        )
        self.decoder3 = DoubleConv(512, 256)

        self.upconv2 = nn.ConvTranspose2d(
            256, 128, kernel_size=2, stride=2
        )
        self.decoder2 = DoubleConv(256, 128)

        self.upconv1 = nn.ConvTranspose2d(
            128, 64, kernel_size=2, stride=2
        )
        self.decoder1 = DoubleConv(128, 64)

        # Output layer
        self.output = nn.Conv2d(
            64,
            num_classes,
            kernel_size=1
        )

    def forward(self, x):

        # Encoder path
        e1 = self.encoder1(x)

        e2 = self.encoder2(
            self.pool(e1)
        )

        e3 = self.encoder3(
            self.pool(e2)
        )

        e4 = self.encoder4(
            self.pool(e3)
        )

        # Bottleneck
        b = self.bottleneck(
            self.pool(e4)
        )

        # Decoder path
        d4 = self.upconv4(b)
        d4 = torch.cat([d4, e4], dim=1)
        d4 = self.decoder4(d4)

        d3 = self.upconv3(d4)
        d3 = torch.cat([d3, e3], dim=1)
        d3 = self.decoder3(d3)

        d2 = self.upconv2(d3)
        d2 = torch.cat([d2, e2], dim=1)
        d2 = self.decoder2(d2)

        d1 = self.upconv1(d2)
        d1 = torch.cat([d1, e1], dim=1)
        d1 = self.decoder1(d1)

        return self.output(d1)


def load_segmentation_model(
    model_path=None,
    device=None
):
    """
    Initialize U-Net and optionally load
    trained model weights.
    """

    if device is None:
        device = torch.device(
            "cuda" if torch.cuda.is_available()
            else "cpu"
        )

    model = UNet()

    if model_path:
        checkpoint = torch.load(
            model_path,
            map_location=device,
            weights_only=True
        )

        model.load_state_dict(checkpoint)

    model.to(device)

    return model


def predict_segmentation(model, image, device=None):
    """
    Generate a land-cover segmentation map.
    """

    if device is None:
        device = next(model.parameters()).device

    model.eval()

    image = torch.as_tensor(
        image,
        dtype=torch.float32,
        device=device
    )

    if image.ndim == 3:
        image = image.unsqueeze(0)

    with torch.no_grad():
        predictions = model(image)
        mask = torch.argmax(
            predictions,
            dim=1
        )

    return mask.squeeze(0).cpu().numpy()
