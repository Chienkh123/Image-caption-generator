# Image Caption Generator

An AI-powered image caption generator that creates natural language descriptions of images using deep learning.

## Features

- Generates descriptive captions for uploaded images
- Supports common image formats (JPG, PNG, JPEG)
- Built with a CNN-LSTM architecture for accurate caption generation
- Easy-to-use interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Chienkh123/image-caption-generator.git
cd image-caption-generator
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Run the application:
```python
python app.py
```

2. Upload an image through the interface
3. Get generated captions for your image

## Model Architecture

The caption generator uses a CNN-LSTM architecture:
- CNN: Extracts image features using a pre-trained model
- LSTM: Generates natural language captions based on the extracted features

## Requirements

- Python 3.7+
- PyTorch
- TensorFlow
- PIL
- NumPy
- Other dependencies listed in requirements.txt

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built using [relevant frameworks/libraries]
- Inspired by [relevant papers/projects]
