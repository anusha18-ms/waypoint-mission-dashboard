from PIL import Image
import os

input_folder = 'images'
output_folder = 'images_resized'

os.makedirs(output_folder, exist_ok=True)

# Target resolution for consistent quality (e.g., 800x600)
target_size = (800, 600)

for image_name in os.listdir(input_folder):
    if image_name.endswith(('jpg', 'jpeg', 'png')):
        img_path = os.path.join(input_folder, image_name)
        img = Image.open(img_path)

        # Resize and maintain aspect ratio
        img.thumbnail(target_size, Image.LANCZOS)

        # Save resized image
        output_path = os.path.join(output_folder, image_name)
        img.save(output_path, quality=95)

print("Images resized successfully!")
