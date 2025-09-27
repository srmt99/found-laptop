from decoder import decode_text

def ask_coordinates():
    """Ask for coordinates until the correct ones are entered"""
    password = "qdMrrorrkfrrNhmrrMudvzrN"

    print("=" * 30)
    print("Meeting Spot Coordinates Required")
    print("Enter the first 2 digits of each coordinate")
    print("Example: 39 N, 12 E")
    print("=" * 30)

    # Ask for N coordinate
    n_attempts = 0
    while True:
        n_attempts += 1
        n_coord = input("Enter first 2 digits of N coordinate: ").strip()

        if decode_text("Nc") == n_coord:
            print("✓ N coordinate correct!\n")
            break
        else:
            if n_attempts >= 5:
                print("\033[91mHint: The meeting spot is in the safe-box!\033[0m")
                n_attempts = 0
            else:
                print("\033[91mIncorrect N coordinate. Try again!\033[0m")

    # Ask for E coordinate
    e_attempts = 0
    while True:
        e_attempts += 1
        e_coord = input("Enter first 2 digits of E coordinate: ").strip()

        if decode_text("Ec") == e_coord:
            print("✓ E coordinate correct!\n")
            print(f"\033[92mAccess granted. Password: {decode_text(password)}\033[0m")
            return True
        else:
            if e_attempts >= 5:
                print("\033[91mHint: The meeting spot is in the safe-box!\033[0m")
                e_attempts = 0
            else:
                print("\033[91mIncorrect E coordinate. Try again!\033[0m")

def main():
    ask_coordinates()

if __name__ == "__main__":
    main()
