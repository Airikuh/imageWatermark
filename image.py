from PIL import Image

def add_watermark(input_image_path, watermark_image_path, output_image_path, position=(0, 0), blend_weight=0.05):
    # Open the input image
    original_image = Image.open(input_image_path)
    # Open the watermark image
    watermark_image = Image.open(watermark_image_path)
    # Ensure that the watermark image has an alpha channel
    if watermark_image.mode != 'RGBA':
        watermark_image = watermark_image.convert('RGBA')
    # Resize the watermark image to fit the original image
    #watermark_image = watermark_image.resize(original_image.size)
    # Create a transparent layer for the watermark
    watermark = Image.new('RGBA', original_image.size, (255, 255, 255, 0))
    # Paste the watermark image onto the transparent layer
    watermark.paste(watermark_image, position, mask=watermark_image)
    # Combine the original image with the watermark
    watermarked_image = Image.blend(original_image.convert('RGBA'), watermark, blend_weight)
 # Convert the result to 'RGB' before saving to avoid an error
    watermarked_image = watermarked_image.convert('RGB')
    # Save the image with the watermark
    watermarked_image.save(output_image_path)
    watermarked_image.show()

if __name__ == "__main__":
    # Replace these paths with your actual file paths
    input_image_path = "fall_michigan.png"
    watermark_image_path = "UMD.png"
    output_image_path = "output_image_with_watermark.png"
# Specify the position of the watermark (optional), The default position is (0, 0), i.e., top-left corner
    #watermark_position = (10, 10)
    #watermark_position = (x, y)
    watermark_position = (900, 10)
# Specify the blending weight of the watermark (0-1), The default transparency is 0.05 (fully opaque)
    watermark_blend_weight = 0.05
    add_watermark(input_image_path, watermark_image_path, output_image_path, watermark_position, watermark_blend_weight)
