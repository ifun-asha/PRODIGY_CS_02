from PIL import Image
import os
import platform
import subprocess

def open_image(output_path):
    """Open the image using the default viewer for the OS."""
    if platform.system() == "Windows":
        os.startfile(output_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", output_path])
    else:  # Linux
        subprocess.run(["xdg-open", output_path])

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            pixels[x,y]= (
            (r + key) % 256,
            (g + key) % 256,
            (b + key) % 256
            )

    image.save(output_path)
    print(f"Image encrypted and saved to {output_path} ")
    open_image(output_path)

def decrypt_image(input_path, output_path, key):
        image = Image.open(input_path)
        pixels = image.load()
        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )

        image.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
        open_image(output_path)

def main():
    print("~ Image Manipulation Tool ~")
    choice = input("Type 'e' to encrypt or 'd' to decrypt an image: ").strip().lower()
    #Ask User for Image Path
    input_path = input("Enter the full path of the image:")
    if not os.path.exists(input_path):
        print("X File not found. Please check the path.")
        return
    output_path = input("Enter the path to save encrypted image:")
    key = int(input("Enter the an encryption key {must be between 0 - 255}:"))
    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    elif choice == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print("X Invalid choice. Please restart and type 'e' or 'd'.")


main()
