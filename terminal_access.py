def decode_text(encoded):
    """Simple text obfuscation - reverse + shift"""
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

def ask_question(question, target_word):
    """Ask a question until the correct answer is given"""
    attempts = 0

    while True:
        attempts += 1
        answer = input(f"{question} ").lower()

        if decode_text(target_word) in answer:
            print("✓ Correct!\n")
            return True
        else:
            if attempts >= 5:
                print(f"\033[91m{decode_text('!vrwrks 3 hkw nfhkf :wqlk')}\033[0m")  # Red hint message
                attempts = 0
            else:
                print("\033[91mTry again!\033[0m")  # Red "Try again!"

def main():
    print("=" * 20)
    print("Laptop Password Authentication")
    print("Answer these questions to unlock the laptop")
    print("=" * 20)

    # Question 1: Food
    ask_question("Food name?", "uhjuxe")

    # Question 2: Clothes
    ask_question("Clothes brand?", "lydp")

    # Question 3: Drink
    ask_question("Caribou (drink)?", "hhiirf")

    # Success message
    print(f"\033[92m{decode_text('kjurphpknrw :2# bhn')}\033[0m")  # Green success message

if __name__ == "__main__":
    main()