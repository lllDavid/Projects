def simple_hash(data):
    hash_value = 0
    for char in data:
        ascii_value = ord(char)
        hash_value ^= (ascii_value * 37)  
        hash_value += ascii_value  
    
    hash_value = hash_value % (2**32)
    return hash_value
password_hash = 2480
password = str(input("Enter password:"))
if simple_hash(password) != password_hash:
    print(f"Wrong")
else:
    print(f"Correct")
