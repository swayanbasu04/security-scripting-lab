from PIL import Image
import numpy as np
import os

def encode_image_to_pixels(image_path, key, file_name, file_format):
    img = Image.open(image_path).convert('RGB')

    img_array = np.array(img)

    key = np.resize(key, img_array.shape)

    encoded_array = np.bitwise_xor(img_array, key)
    encoded_img = Image.fromarray(encoded_array.astype('uint8'), 'RGB')

    encoded_img.save(f"encoded_{file_name}.{file_format}")
    print(f"Encoded image saved to encoded_{file_name}.{file_format}")
    return f"encoded_{file_name}.{file_format}"


def decode_pixels_to_image(encoded_image_path, key, file_name, file_format):
    encoded_img = Image.open(encoded_image_path).convert('RGB')
    encoded_array = np.array(encoded_img)
    
    key = np.resize(key, encoded_array.shape)
    decoded_array = np.bitwise_xor(encoded_array, key)

    decoded_img = Image.fromarray(decoded_array.astype('uint8'), 'RGB')
    decoded_img.save(f"decoded_{file_name}.{file_format}")
    print(f"Decoded image saved to decoded_{file_name}.{file_format}")    


def main():
    print("Pixel-level Image Encoder/Decoder")
    image_path = input("Enter the path of the image to encode: ")
    if not os.path.isfile(image_path):
        print(f"[!] Error: File not found: {image_path}")
        return
    try:
        key_value = int(input("Enter an integer key for encoding/decoding: "))
    except ValueError:
        print("[!] Error: key must be an integer")
        return

    file_name = input("Choose name for the encoded image: ")
    file_format = "png"

    try:
        np.random.seed(key_value)
        key = np.random.randint(0, 256, size=(1, 1, 3), dtype=np.uint8)

        encoded_path = encode_image_to_pixels(image_path, key, file_name, file_format)
        decode_pixels_to_image(encoded_path, key, file_name, file_format)
    except Exception as exc:
        print(f"[!] Encoding failed: {exc}")

if __name__ == "__main__":
    main()
