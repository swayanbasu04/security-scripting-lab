## Image Encryption and Decryption

This project encrypts an image at the pixel level using a simple XOR-based process and then decrypts it back using the same integer key.

## Requirements

- Python 3
- `Pillow`
- `numpy`

Install the dependencies with:

```bash
pip install pillow numpy
```

## How to Run

Run the script with Python:

```bash
python image_encrypt.py
```

## What the Script Does

The program will:

1. Ask for the path of the image to encode
2. Ask for an integer key
3. Ask for a name for the output file
4. Create an encoded image named `encoded_<name>.png`
5. Create a decoded image named `decoded_<name>.png`

## Notes

- The script works with RGB images.
- The output format is always PNG.
- Use the same integer key to encode and decode the image.

  

                                  ----------------_______----------------
