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
            print("bad option, Please select one between 1 y 5")

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
                print(f"Your generated password is -> ", ''.join(password), f", and have {largoContra} characters")
            elif level1_userOption == 2:
                print("you would be returned to the menu")
                return self.menu()
            else: 
                print("You pressed for exit")
                breakpoint
        else:
            print("invalid option. please enter a number between 1 and 3")

    def level2(self):
        print("You selected level one to create your password.")
        print("Type (1) to confirm your selection, (2) to return to the menu, (3) to exit the code.")  
        level1_userOption = int(input("Please enter your option: "))
        if 1 <= level1_userOption <= 3: 
            if level1_userOption == 1:
                print("You confirm your selection!!!")
                largo1 = random.randint(16, 20)
                for i in range(largo1):
                    password.append(random.choice(characters))
                    largoContra = len(password)
                print(f"Your generated password is -> ", ''.join(password), f", and have {largoContra} characters")
            elif level1_userOption == 2:
                print("you would be returned to the menu")
                return self.menu()
            else: 
                print("You pressed for exit")
                breakpoint
        else:
            print("invalid option. please enter a number between 1 and 3")

    def level3(self):
        print("You selected level one to create your password.")
        print("Type (1) to confirm your selection, (2) to return to the menu, (3) to exit the code.")  
        level1_userOption = int(input("Please enter your option: "))
        if 1 <= level1_userOption <= 3: 
            if level1_userOption == 1:
                print("You confirm your selection!!!")
                largo1 = random.randint(24, 29)
                for i in range(largo1):
                    password.append(random.choice(characters))
                    largoContra = len(password)
                print(f"Your generated password is -> ", ''.join(password), f", and have {largoContra} characters")
            elif level1_userOption == 2:
                print("you would be returned to the menu")
                return self.menu()
            else: 
                print("You pressed for exit")
                breakpoint
        else:
            print("invalid option. please enter a number between 1 and 3")

    def level4(self):
        print("You selected level one to create your password.")
        print("Type (1) to confirm your selection, (2) to return to the menu, (3) to exit the code.")  
        level1_userOption = int(input("Please enter your option: "))
        if 1 <= level1_userOption <= 3: 
            if level1_userOption == 1:
                print("You confirm your selection!!!")
                largo_selection = int(input("Enter how many characters you want: "))
                for i in range(largo_selection):
                    password.append(random.choice(characters))
                    largoContra = len(password)
                print(f"Your generated password is -> ", ''.join(password), f", and have {largoContra} characters")
            elif level1_userOption == 2:
                print("you would be returned to the menu")
                return self.menu()
            else: 
                print("You pressed for exit")
                breakpoint
        else:
            print("invalid option. please enter a number between 1 and 3")


password_gen = Password_gen()
password_gen.menu()
#password_gen.Level1()