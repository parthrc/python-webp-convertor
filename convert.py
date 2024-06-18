import os
from PIL import Image

# Function to convert image to WebP format
def convert_to_webp(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            img.save(output_path, format='webp')
            print(f"Converted {image_path} to {output_path}")
    except Exception as e:
        print(f"Failed to convert {image_path}: {e}")

# Get the current directory
current_dir = os.getcwd()

# Supported image extensions
supported_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']

# Create a new directory for the converted images
output_dir = os.path.join(current_dir, 'converted_images')
os.makedirs(output_dir, exist_ok=True)

# Cpunt total images converted
images_count = 0

# Loop through files in the current directory
for filename in os.listdir(current_dir):
    
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in supported_extensions:
        images_count += 1
        input_path = os.path.join(current_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '_webp.webp')
        convert_to_webp(input_path, output_path)
    
print(f"Total images converted: {images_count}")
