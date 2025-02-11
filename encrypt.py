
import cv2
import os
import numpy as np

# Load the image
img_path = r"C:\Users\ashik\Downloads\Stenography-main\Stenography-main\Screenshot (12).png"
img = cv2.imread(img_path)

if img is None:
    print("Error: Could not read the image. Check the file path.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# ASCII mappings
d = {chr(i): i for i in range(255)}

# Image dimensions
height, width, _ = img.shape  

n, m, z = 0, 0, 0  # Initialize pixel positions

# Store message length in the first pixel (ensure it doesn't exceed 254)
msg_length = min(len(msg), 254)
img[0, 0, 0] = msg_length

# Encoding message into image
for char in msg[:msg_length]:  # Only encode up to the valid length
    img[n, m, z] = np.uint8(d[char])  # Ensure value is uint8
    n = (n + 1) % height
    m = (m + 1) % width
    z = (z + 1) % 3  # Cycle through BGR channels

# Save encrypted image
output_path = r"C:\Users\ashik\Downloads\Stenography-main\Stenography-main\encryptedImage.png"
cv2.imwrite(output_path, img)  # Save as PNG to avoid compression issues
print(f"Message encrypted and saved in {output_path}")

# Open image
os.system(f"start {output_path}")
