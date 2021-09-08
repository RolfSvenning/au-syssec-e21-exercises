from ppmcrypt import PPMImage

key = bytes(16)
print(key)

image = PPMImage.load_from_file(open('dk.ppm', 'rb'))
image.encrypt(key, 'ecb')
image.data[:3 * 5000] = bytes.fromhex('0000FF') * 5000
image.decrypt(key)
image.write_to_file(open('image_encrypted.ppm', 'wb'))