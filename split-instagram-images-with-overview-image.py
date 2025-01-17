import sys
import os
from PIL import Image

def split_image(input_path):
    """
    Splits an image into vertical slices depending on its aspect ratio:
      • ~12:5 → 3 slices
      • ~8:5  → 2 slices
    Suffixes for the slices are added to the original file name.
    """
    img = Image.open(input_path)
    width, height = img.size
    ratio = width / float(height)

    # Decide how many slices based on ratio
    def is_close(a, b, tol=1e-2):
        return abs(a - b) < tol

    if is_close(ratio, 2.4):  # ~12:5
        n_slices = 3
    elif is_close(ratio, 1.6):  # ~8:5
        n_slices = 2
    else:
        raise ValueError(f"Unsupported aspect ratio: {ratio:.2f}")

    slice_width = width / float(n_slices)

    # Extract base filename and extension
    base_name, ext = os.path.splitext(input_path)

    # Create slices and save with suffix
    for i in range(n_slices):
        left = int(i * slice_width)
        right = int((i + 1) * slice_width)
        slice_img = img.crop((left, 0, right, height))
        slice_img.save(f"output/{base_name}_slice_{i+1}{ext}")

def create_overview_image(input_path, border_percent=0.05):
    """
    Creates a 4:5 ratio overview image containing the full original image.
    Handles both 12:5 and 8:5 images.
    Adds a "_overview" suffix to the original file name.
    """
    original = Image.open(input_path)
    w_in, h_in = original.size
    ratio = w_in / float(h_in)

    # Decide how to handle aspect ratios dynamically
    def is_close(a, b, tol=1e-2):
        return abs(a - b) < tol

    if is_close(ratio, 2.4):  # ~12:5
        border_px = int(border_percent * w_in)
        w_final = w_in + 2 * border_px
    elif is_close(ratio, 1.6):  # ~8:5
        border_px = int(border_percent * w_in)
        w_final = w_in + 2 * border_px
    else:
        raise ValueError(f"Unsupported aspect ratio: {ratio:.2f}")

    # Calculate the final height based on 4:5 ratio
    h_final = int((5.0 / 4.0) * w_final)

    # Create the overview canvas with a white background
    overview_img = Image.new("RGB", (w_final, h_final), (255, 255, 255))

    # Center the original image in the overview
    left_offset = border_px
    top_offset = (h_final - h_in) // 2

    # Paste the original image onto the overview canvas
    overview_img.paste(original, (left_offset, top_offset))

    # Save the overview image with a suffix
    base_name, ext = os.path.splitext(input_path)
    overview_img.save(f"output/{base_name}_overview{ext}")

def main():
    # Check if the script was run with the correct arguments
    if len(sys.argv) != 2:
        print("Usage: split-instagram-images-with-overview-image.py <image_path>")
        sys.exit(1)

    # Get the image path from the command-line arguments
    image_path = sys.argv[1]
    os.makedirs("output", exist_ok=True)
    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    # Run the processing functions
    try:
        split_image(image_path)
        create_overview_image(image_path, border_percent=0.05)
        print(f"Processing complete for '{image_path}'.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()