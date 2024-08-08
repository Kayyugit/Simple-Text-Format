def capitalize_text(text):
    return ' '.join(word.capitalize() for word in text.split())

def uppercase_text(text):
    return text.upper()

def lowercase_text(text):
    return text.lower()

def text_format():
    print("Simple Text Format")
    while True:
        print("\nPlease choose an option:")
        print("1. Capitalize each word")
        print("2. Convert text to uppercase")
        print("3. Convert text to lowercase")
        print("4. Exit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == '1':
            text = input("\nEnter the text to capitalize each word: ")
            print("Capitalized Text:")
            print(capitalize_text(text))
        elif choice == '2':
            text = input("\nEnter the text to convert to uppercase: ")
            print("Uppercase Text:")
            print(uppercase_text(text))
        elif choice == '3':
            text = input("\nEnter the text to convert to lowercase: ")
            print("Lowercase Text:")
            print(lowercase_text(text))
        elif choice == '4':
            print("Text Format Exited")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    text_format()
