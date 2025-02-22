# Decryption Code

import cv2

def decrypt_image(image_path, password):
    img = cv2.imread(image_path)
    c = {}
    for i in range(255):
        c[i] = chr(i)

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        n, m, z = 0, 0, 0
        message = ""
        for i in range(100):  
            message += c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT auth")

image_path = "encryptedImage.jpg"
password = input("Enter the passcode used during encryption: ")

decrypt_image(image_path, password)
