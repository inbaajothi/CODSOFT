import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("The length of the password should be positive integer")
        password = generate_password(length)
        print("Generated Password:", password)
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
