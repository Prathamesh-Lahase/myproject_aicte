# Encryption Code

import cv2

def encrypt_image(image_path, secret_message, password):
    img = cv2.imread(image_path)
    d = {}
    for i in range(255):
        d[chr(i)] = i

    n, m, z = 0, 0, 0
    for i in range(len(secret_message)):
        img[n, m, z] = d[secret_message[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)

image_path = "mypic.jpg"
secret_message = input("Enter secret message: ")
password = input("Enter a passcode: ")

encrypt_image(image_path, secret_message, password)
