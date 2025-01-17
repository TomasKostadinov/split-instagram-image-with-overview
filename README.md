# Image Splitter and Overview Generator

This Python script splits an input image into vertical slices and generates an overview image with a 4:5 aspect ratio. It supports images with the following aspect ratios:
- **12:5** (split into 3 slices)
- **8:5** (split into 2 slices)

The script is designed for command-line usage, allowing you to easily process images by specifying their file paths.

## Features

- Automatically detects the aspect ratio of the input image.
- Splits the image into 2 or 3 slices based on its aspect ratio.
- Creates a 4:5 overview image with configurable borders.
- Preserves the original filename by appending suffixes (`_slice_N`, `_overview`).

## Prerequisites

- Python 3.7 or higher
- [Pillow (PIL)](https://python-pillow.org/) library for image processing.

Install Pillow with:
```bash
pip install pillow
```

## Usage

Run the script from the command line with the path to the image as an argument:

```bash
python3 split-instagram-images-with-overview-image.py <image_path>
```

## Example

For an image named example.jpg in the same directory as the script:

python3 split-instagram-images-with-overview-image.py example.jpg

## Output Files

For example.jpg:

    Slices:
        example_slice_1.jpg
        example_slice_2.jpg (or 3 slices for 12:5 images)
    Overview:
        example_overview.jpg
