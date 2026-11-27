
# System Limitations and Considerations

## 1. Model Training

The project includes a U-Net architecture and training pipeline, but no verified trained model weights are included.

Predictions require a properly trained and evaluated model.

## 2. Dataset Dependency

Model performance depends on:

- Dataset quality
- Image resolution
- Label accuracy
- Geographic diversity
- Sensor characteristics
- Training and validation methodology

## 3. Change Detection

The current change-detection implementation is a pixel-level comparison baseline.

It does not independently identify deforestation, flooding, or urban expansion.

Reliable comparisons require:
- Spatial co-registration
- Comparable image resolution
- Consistent image preprocessing
- Similar acquisition conditions
- Appropriate handling of seasonal and atmospheric differences

## 4. Geospatial Accuracy

Area calculations depend on:
- Valid coordinate reference systems
- Correct raster transforms
- Suitable projected coordinate systems
- Correct alignment between masks and source imagery

## 5. Multi-Spectral Imagery

The current preprocessing pipeline primarily uses three image channels.

Specialized multi-spectral analysis requires additional band-handling and model modifications.

## 6. Security

Before public deployment, the application requires further security review, including:

- Upload content validation
- Authentication and authorization
- Secure secret management
- File retention policies
- Request rate limiting
- Production server configuration

## 7. Scientific Validation

The system should be treated as a research and development project.

Do not use its outputs as the sole basis for environmental, emergency-response, financial, or regulatory decisions without independent validation.

## 8. Future Improvements

- Geospatially aware change detection
- Multi-spectral deep learning
- More robust model evaluation
- Geographic visualization
- Automated reporting
- Production-grade security
