from auth import hash_password, verify_password

password = "mypassword123"

hashed = hash_password(password)

print("Hash:", hashed)

print("Correct:",
      verify_password(password, hashed))

print("Wrong:",
      verify_password("wrongpassword", hashed))