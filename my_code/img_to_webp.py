import os
try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Installing now...")
    os.system("python -m pip install pillow")
    from PIL import Image

# --- Determine paths relative to this script ---
script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where this script is
input_folder = os.path.join(script_dir, "img")          # "img" folder in the same folder as this script
output_folder = os.path.join(script_dir, "webp_images") # output folder

quality = 80  # WebP quality

# Make output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert images
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_folder, filename)
        output_name = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(output_folder, output_name)

        # Skip if already converted
        if os.path.exists(output_path):
            print(f"Skipping (already exists): {output_name}")
            continue

        with Image.open(input_path) as img:
            img.save(output_path, "WEBP", quality=quality)

        print(f"Converted: {filename} -> {output_name}")
