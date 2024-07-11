import hashlib

class PasswordPair:

    def __init__(self):
        self.clave = None

    def menu(self):
        print("Welcome to the password pair finder")
        print("The instructions for this code are simple: first you transform your password to some encrypted type, and after you compare it with the dictionary of passwords found on the internet.")
        print("Enter the hash you want to resolve")
        self.clave = input("Enter the hash: ")
        self.menu2()

    def menu2(self):
        print("You can download a password dictionary and provide the path where the txt file is located. If you don't have it, we have a default one.")
        user_choice = input("If you have a dictionary, copy the path here. If you don't have one, type 2: ")
        if user_choice == "2":
            self.default_path = "C:/Users/CHK/Downloads/10-million-password-list-top-100000.txt"
        else:
            self.default_path = user_choice

        self.main()

    def main(self):
        user_encrypt = int(input("Menu options\n1 - for MD5\n2 - for SHA1\n3 - for SHA224\n4 - for SHA256\n5 - for SHA384\n6 - for SHA512\nEnter the number corresponding to the type of encryption you want to use: "))

        if user_encrypt in [1, 2, 3, 4, 5, 6]:
            self.pair(self.clave, user_encrypt)
        else:
            print("Invalid option selected.")

    def pair(self, resolvehash, hash_type):
        with open(self.default_path, 'r') as resolver:
            for x in resolver:
                a = x.strip("\n")
                
                if hash_type == 1:
                    hashed = hashlib.md5(a.encode()).hexdigest()
                elif hash_type == 2:
                    hashed = hashlib.sha1(a.encode()).hexdigest()
                elif hash_type == 3:
                    hashed = hashlib.sha224(a.encode()).hexdigest()
                elif hash_type == 4:
                    hashed = hashlib.sha256(a.encode()).hexdigest()
                elif hash_type == 5:
                    hashed = hashlib.sha384(a.encode()).hexdigest()
                elif hash_type == 6:
                    hashed = hashlib.sha512(a.encode()).hexdigest()
                else:
                    print("Invalid hash type.")
                    return
                
                if hashed == resolvehash:
                    print(f"Password: {a} - This hash was resolved: {hashed}")
                    break  # Stops searching if the hash is found
            else:
                print("No match found for the given hash.")

if __name__ == '__main__':
    finder = PasswordPair()
    finder.menu()
