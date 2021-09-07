from ppmcrypt import PPMImage

dk_relative_path = "au-syssec-e21-exercises/01_symmetric_encryption/dk.ppm"
image = PPMImage.load_from_file(open(dk_relative_path, 'rb'))
print(f'image width: {image.width} px')
print(f'image height: {image.height} px')
print(f'first 16 bytes of that data: {image.data[:16].hex()}')
# make the first 1000 pixel blue
image.data[:3 * 1000] = bytes.fromhex('0000FF') * 1000
image.write_to_file(open('new_image.ppm', 'wb'))