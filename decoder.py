import base64

with open('a.txt', 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_decode = base64.decodestring(binary_file_data)
    image_result = open('olatest4.apk','wb')
    image_result.write(base64_decode)

