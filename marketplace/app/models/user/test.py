import pyotp
import qrcode

# Step 1: Generate a secret key using pyotp
totp = pyotp.TOTP(pyotp.random_base32())  # Generate a random secret key
secret_key = totp.secret

# Step 2: Create a URI that can be scanned by an authenticator app
# For this example, the issuer and user name will be 'ExampleApp' and 'user@example.com'
uri = totp.provisioning_uri("user@example.com", issuer_name="ExampleApp")

# Step 3: Generate a QR Code using the qrcode library
qr = qrcode.make(uri)

# Save the QR code as an image
qr.save("2fa_qr_code.png")

# Print the secret key for manual setup if needed
print("Your secret key is:", secret_key)
print("A QR code has been generated and saved as '2fa_qr_code.png'.")
