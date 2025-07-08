# validate user input exercise

print("option 1 is the more complex version of the program and option 2 is the simpler version of the program")
choice = input("do you want version 1 or 2 of the program? ")
if choice == "1":
    def space_check(username):
      if " " in username:
        print("username cannot contain spaces")
        return False
      return True    

    def digit_check(username):
       if username.isalpha():
        return True
       else:
        print("username cannot contain digits")
        return False

    def character_check(username):
       if len(username) <= 12:
        return True
       else:
        print("username is too long")
        print("username must be less than 12 characters")
        return False

    def validate_username(username):
        print(f"Validating username: {username}")
        print("--- Validation Results ---")
        valid_space = space_check(username)
        valid_digits = digit_check(username)
        valid_length = character_check(username)
        
        if valid_space and valid_digits and valid_length:
            print("username is valid")
            return True
        else:
            print("username is invalid")
            return False

    def main():
        while True:
            username = input("Enter your username (or 'quit' to exit): ")
            
            if username.lower() == 'quit':
                print("Goodbye!")
                break
                
            validate_username(username)
            print("       ")

    if __name__ == "__main__":
        main()

if choice == "2":
    user = input("Enter your username: ")
    if len(user) > 12:
        print("your username cant be more than 12 characters")
    elif not user.find(" ") == "-1":
        print("your username cant have spaces")
    elif not user.isalpha():
        print("your username cant have digits")
    else:
        print(f"wellcome {user}")
