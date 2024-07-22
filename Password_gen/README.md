# Password Generator

This is a small project in Python for generating passwords of different complexity levels. The main goal of this project is to provide a practical tool for creating secure passwords, as well as to serve as an educational exercise for those interested in programming with Python.

## Description

The password generator offers four levels of complexity:

- **Level 1**: Generates a short password between 10 and 14 characters.
- **Level 2**: Generates a medium-level password between 16 and 20 characters.
- **Level 3**: Generates a complex password between 24 and 28 characters.
- **Level 4**: Allows the user to select the password length, with a minimum of 8 characters and a maximum of 60 characters.

## Requirements

- Python 3.x

## Installation

Clone this repository and run the script to start generating passwords.

```bash
git clone https://github.com/your_username/password_generator.git
cd password_generator
python password_generator.py
```

## Usage

Run the `password_generator.py` script and follow the on-screen instructions to generate your password.

```python
import random
import string

password = []
characters = string.ascii_letters + string.digits + string.punctuation
largoContra = len(password)

class Password_gen:
    def __init__(self):
        pass

    def menu(self):
        print("Welcome to the Password Generator!!!\nIn this code, you have 4 options to generate your password:\nLevel 1 - You have a short password between 10 to 14 characters.\nLevel 2 - You have a medium-level password between 16 to 20 characters.\nLevel 3 - You can create a more complex one between 24 to 28 characters.\nLevel 4 - The personalized one, you can select the length of the password with a minimum of 8 characters and a maximum of 60 characters. \nPress 5 to exit \n(It is recommended to have a password with more than 12 characters.)")
        Useroption = int(input("Select what type of level Password you need: "))
        if Useroption == 1:
            return self.level1()
        elif Useroption == 2:
            return self.level2()
        elif Useroption == 3:
            return self.level3()
        elif Useroption == 4:
            return self.level4()
        elif Useroption == 5:
            breakpoint
        else:
            print("Bad option, please select one between 1 and 5")

    def level1(self):
        print("You selected level one to create your password.")
        print("Type (1) to confirm your selection, (2) to return to the menu, (3) to exit the code.")  
        level1_userOption = int(input("Please enter your option: "))
        if 1 <= level1_userOption <= 3: 
            if level1_userOption == 1:
                print("You confirm your selection!!!")
                largo1 = random.randint(10, 14)
                for i in range(largo1):
                    password.append(random.choice(characters))
                    largoContra = len(password)
                print(f"Your generated password is -> ", ''.join(password), f", and has {largoContra} characters")
            elif level1_userOption == 2:
                print("You will be returned to the menu")
                return self.menu()
            else: 
                print("You pressed to exit")
                breakpoint
        else:
            print("Invalid option. Please enter a number between 1 and 3")

    def level2(self):
        print("You selected level two to create your password.")
        print("Type (1) to confirm your selection, (2) to return to the menu, (3) to exit the code.")  
        level2_userOption = int(input("Please enter your option: "))
        if 1 <= level2_userOption <= 3: 
            if level2_userOption == 1:
                print("You confirm your selection!!!")
                largo2 = random.randint(16, 20)
                for i in range(largo2):
                    password.append(random.choice(characters))
                    largoContra = len(password)
                print(f"Your generated password is -> ", ''.join(password), f", and has {largoContra} characters")
            elif level2_userOption == 2:
                print("You will be returned to the menu")
                return self.menu()
            else: 
                print("You pressed to exit")
                breakpoint
        else:
            print("Invalid option. Please enter a number between 1 and 3")

    def level3(self):
        print("You selected level three to create your password.")
        print("Type (1) to confirm your selection, (2) to return to the menu, (3) to exit the code.")  
        level3_userOption = int(input("Please enter your option: "))
        if 1 <= level3_userOption <= 3: 
            if level3_userOption == 1:
                print("You confirm your selection!!!")
                largo3 = random.randint(24, 28)
                for i in range(largo3):
                    password.append(random.choice(characters))
                    largoContra = len(password)
                print(f"Your generated password is -> ", ''.join(password), f", and has {largoContra} characters")
            elif level3_userOption == 2:
                print("You will be returned to the menu")
                return self.menu()
            else: 
                print("You pressed to exit")
                breakpoint
        else:
            print("Invalid option. Please enter a number between 1 and 3")

    def level4(self):
        print("You selected level four to create your password.")
        print("Type (1) to confirm your selection, (2) to return to the menu, (3) to exit the code.")  
        level4_userOption = int(input("Please enter your option: "))
        if 1 <= level4_userOption <= 3: 
            if level4_userOption == 1:
                print("You confirm your selection!!!")
                largo_selection = int(input("Enter how many characters you want: "))
                for i in range(largo_selection):
                    password.append(random.choice(characters))
                    largoContra = len(password)
                print(f"Your generated password is -> ", ''.join(password), f", and has {largoContra} characters")
            elif level4_userOption == 2:
                print("You will be returned to the menu")
                return self.menu()
            else: 
                print("You pressed to exit")
                breakpoint
        else:
            print("Invalid option. Please enter a number between 1 and 3")

password_gen = Password_gen()
password_gen.menu()
```

## Contributing

Contributions are welcome. If you want to improve this project or add new features, please follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
