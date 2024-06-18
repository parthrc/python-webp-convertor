import os
from PIL import Image
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to convert image to WebP format
def convert_to_webp(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            img.save(output_path, format='webp')
            print(f"Converted {image_path} to {output_path}")
            return True
    except Exception as e:
        print(f"Failed to convert {image_path}: {e}")
        return False

# Function to process all images in the given directory
def process_directory(input_dir, output_dir):
    # Supported image extensions
    supported_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Count images
    images_count = 0

    # Iterate through files in the input directory
    for filename in os.listdir(input_dir):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension in supported_extensions:
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')
            conversion = convert_to_webp(input_path, output_path)
            if(conversion):
                images_count += 1 
                
    return images_count

# Function to handle the GUI
def run_gui():
    def select_input_dir():
        input_dir = filedialog.askdirectory()
        if input_dir:
            input_dir_entry.delete(0, tk.END)
            input_dir_entry.insert(0, input_dir)

    def select_output_dir():
        output_dir = filedialog.askdirectory()
        if output_dir:
            output_dir_entry.delete(0, tk.END)
            output_dir_entry.insert(0, output_dir)

    def start_conversion():
        input_dir = input_dir_entry.get()
        output_dir = output_dir_entry.get()
        if not input_dir or not output_dir:
            messagebox.showerror("Error", "Both input and output directories must be selected.")
            return
        total_converted = process_directory(input_dir, output_dir)
        messagebox.showinfo("Success", f"Total images converted: {total_converted}")

    # Set up the GUI window
    window = tk.Tk()
    window.title("Image to WebP Converter")

    tk.Label(window, text="Input Directory:").grid(row=0, column=0, padx=5, pady=5)
    input_dir_entry = tk.Entry(window, width=50)
    input_dir_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=select_input_dir).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(window, text="Output Directory:").grid(row=1, column=0, padx=5, pady=5)
    output_dir_entry = tk.Entry(window, width=50)
    output_dir_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=select_output_dir).grid(row=1, column=2, padx=5, pady=5)

    tk.Button(window, text="Convert", command=start_conversion).grid(row=2, columnspan=3, pady=10)

    window.mainloop()

# Function to handle the CLI
def run_cli():
    parser = argparse.ArgumentParser(description="Convert images to WebP format.")
    parser.add_argument("input_dir", help="Directory containing images to convert.")
    parser.add_argument("output_dir", help="Directory to save converted WebP images.")
    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)

if __name__ == "__main__":
    # Check if the script is being run from the command line or as a standalone program
    import sys
    if len(sys.argv) > 1:
        run_cli()
    else:
        run_gui()
