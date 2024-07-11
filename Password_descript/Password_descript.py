import hashlib

class PasswordPair:

    def __init__(self):
        self.clave = None

    def menu(self):
        print("Welcome to the password pair finder")
        print("The instructions for this code are simple: first you transform your password to some encrypted type, and after you compare it with the dictionary of passwords found on the internet.")
        print("Enter your password")
        self.clave = input("Enter the password: ")
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
        if not self.clave:
            print("No password provided.")
            return

        clave_bytes = self.clave.encode()

        user_encrypt = int(input("Menu options\n1 - for MD5\n2 - for SHA1\n3 - for SHA224\n4 - for SHA256\n5 - for SHA384\n6 - for SHA512\n7 - for using all options\nEnter the number corresponding to the type of encryption you want to use: "))

        if user_encrypt == 1:
            md5 = hashlib.md5(clave_bytes).hexdigest()
            print("Hash MD5 : " + md5)
            self.pair(md5, user_encrypt)
        elif user_encrypt == 2:
            sha1 = hashlib.sha1(clave_bytes).hexdigest()
            print("Hash SHA1 : " + sha1)
            self.pair(sha1, user_encrypt)
        elif user_encrypt == 3:
            sha224 = hashlib.sha224(clave_bytes).hexdigest()
            print("Hash SHA224 : " + sha224)
            self.pair(sha224, user_encrypt)
        elif user_encrypt == 4:
            sha256 = hashlib.sha256(clave_bytes).hexdigest()
            print("Hash SHA256 : " + sha256)
            self.pair(sha256, user_encrypt)
        elif user_encrypt == 5:
            sha384 = hashlib.sha384(clave_bytes).hexdigest()
            print("Hash SHA384 : " + sha384)
            self.pair(sha384, user_encrypt)
        elif user_encrypt == 6:
            sha512 = hashlib.sha512(clave_bytes).hexdigest()
            print("Hash SHA512 : " + sha512)
            self.pair(sha512, user_encrypt)
        elif user_encrypt == 7:
            md5 = hashlib.md5(clave_bytes).hexdigest()
            print("Hash MD5 : " + md5)
            self.pair(md5, 1)
            
            sha1 = hashlib.sha1(clave_bytes).hexdigest()
            print("Hash SHA1 : " + sha1)
            self.pair(sha1, 2)

            sha224 = hashlib.sha224(clave_bytes).hexdigest()
            print("Hash SHA224 : " + sha224)
            self.pair(sha224, 3)

            sha256 = hashlib.sha256(clave_bytes).hexdigest()
            print("Hash SHA256 : " + sha256)
            self.pair(sha256, 4)

            sha384 = hashlib.sha384(clave_bytes).hexdigest()
            print("Hash SHA384 : " + sha384)
            self.pair(sha384, 5)

            sha512 = hashlib.sha512(clave_bytes).hexdigest()
            print("Hash SHA512 : " + sha512)
            self.pair(sha512, 6)
        else:
            print("Invalid option selected.")
            return

    def pair(self, resolvehash, hash_type):
        hash_name = {
            1: "MD5",
            2: "SHA1",
            3: "SHA224",
            4: "SHA256",
            5: "SHA384",
            6: "SHA512"
        }
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
                    print(f"Password: {a} - This hash ({hash_name[hash_type]}) was resolved: {hashed}")
                    break  # Stops searching if the hash is found
            else:
                print(f"No match found for the given hash with type {hash_name[hash_type]}.")

if __name__ == '__main__':
    finder = PasswordPair()
    finder.menu()
