
import cv2

# Load the encrypted image
img_path = r"C:\Users\ashik\Downloads\Stenography-main\Stenography-main\encryptedImage.png"
img = cv2.imread(img_path)

if img is None:
    print("Error: Could not read the encrypted image.")
    exit()

password = input("Enter passcode for Decryption: ")

# ASCII mappings (handle out-of-range values safely)
c = {i: chr(i) for i in range(255)}

# Get message length from the first pixel
msg_length = min(int(img[0, 0, 0]), 254)  # Ensure valid message length

message = ""
n, m, z = 0, 0, 0  # Reset pixel positions

for _ in range(msg_length):  # Read only up to the stored message length
    decrypted_char = c.get(int(img[n, m, z]), "?")  # Handle invalid values safely
    message += decrypted_char
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

print("Decrypted message:", message)
