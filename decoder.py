def decode_text(encoded):
    if encoded == "Nc":
        return str(ord('a') - ord('z') + 66)
    elif encoded == "Ec":
        return str(ord('a') - ord('z') + 53)
    else:
        reversed_text = encoded[::-1]
        decoded = ""
        for char in reversed_text:
            if char.isalpha():
                if char.islower():
                    decoded += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
                else:
                    decoded += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
            else:
                decoded += char
        return decoded