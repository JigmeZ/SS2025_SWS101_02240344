def atbash_cipher(text):# Initialize an empty string to store the output
    output = "" 
    for char in text.upper(): # Convert the input text to uppercase and iterate through each character
        if 'A' <= char <= 'Z': # Check if the character is an uppercase letter
            mirrored = chr(90 - (ord(char) - 65))  # 90 is ASCII for 'Z'
            output += mirrored # Append the mirrored character to the output
        else:
            # If the character is not a letter, append it as is
            output += char
    # Return the final text
    return output

# Practise
message = "JIGME"  
ciphered = atbash_cipher(message)  
print("Encrypted:", ciphered)  
print("Decrypted:", atbash_cipher(ciphered))
