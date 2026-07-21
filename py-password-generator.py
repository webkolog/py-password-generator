#v2.1
import secrets, string

def generate_password():
    print("--- Secure Password Generator ---")
    
    # Get password length from user
    while True:
        try:
            length = int(input("Enter password length (e.g., 4, 6, 20): "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get character type preference
    print("\nSelect character type:")
    print("1: Numbers only (0-9)")
    print("2: Letters only (a-z, A-Z)")
    print("3: Alphanumeric (Letters + Numbers)")
    print("4: Alphanumeric + Symbols (Most Secure)")
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            break
        print("Invalid choice. Please select a number between 1 and 4.")

    # Define character pool based on choice
    if choice == '1':
        char_pool = string.digits
    elif choice == '2':
        char_pool = string.ascii_letters
    elif choice == '3':
        char_pool = string.ascii_letters + string.digits
    else:
        char_pool = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    
    # Print the result
    print("\n" + "="*30)
    print("Your secure password:")
    print(password)
    print("="*30)

def main():
    while True:
        generate_password()
        
        # The area to decide whether to create a new password
        again = input("\nWould you like to generate another password? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()