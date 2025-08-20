from PIL import Image

def check_image_mode(image_path):
    img = Image.open(image_path)
    print(f"{image_path} - Mode: {img.mode}")
    if img.mode == 'RGB':
        print("Gambar ini sudah dalam format 3-channel (RGB).")
    else:
        print("Gambar ini bukan dalam format 3-channel (RGB).")

# Contoh penggunaan
check_image_mode('D:/SIBI/Datas/RGB_converted/A/1645707900.4206524.jpg')
