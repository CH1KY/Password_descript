# Password Pair Finder

## Description

The **Password Pair Finder** program allows users to input a hash they want to resolve and compares it with a dictionary of hashed passwords. If a match is found, the corresponding password is displayed.

## Features

1. **Hash Input**: Users can input a hash they wish to resolve.
2. **Dictionary Selection**: Users can provide a path to a password dictionary or use a default one.
3. **Hash Type Selection**: Users can select from various hash algorithms (MD5, SHA1, SHA224, SHA256, SHA384, SHA512).
4. **Hash Comparison**: The program compares the input hash with hashes of passwords in the dictionary and displays the corresponding password if a match is found.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the files.
2. Ensure you have a password dictionary in `.txt` format.
3. Run the program:

    ```bash
    python password_pair_finder.py
    ```

4. Follow the on-screen instructions.

## Code

```python
import hashlib

class PasswordPair:

    def __init__(self):
        self.clave = None

    def menu(self):
        print("Welcome to the password pair finder")
        print("The instructions for this code are simple: first you enter the hash you want to resolve, and then you compare it with a dictionary of hashed passwords.")
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
        hash_name = {
            1: "MD5",
            2: "SHA1",
            3: "SHA224",
            4: "SHA256",
            5: "SHA384",
            6: "SHA512"
        }
        with open(self.default_path, 'r') as resolvedor:
            for x in resolvedor:
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
                print(f"No match found for the given hash with {hash_name[hash_type]} type.")

if __name__ == '__main__':
    finder = PasswordPair()
    finder.menu()
```

## Code Details

### `PasswordPair` Class

#### Methods

- **`__init__(self)`**: Initializes the instance with the `clave` variable set to `None`.
- **`menu(self)`**: 
  - Prints the welcome message and instructions.
  - Prompts the user to enter a hash they want to resolve.
  - Calls the `menu2` method.
- **`menu2(self)`**: 
  - Asks the user for the path to a password dictionary or uses a default one.
  - Calls the `main` method.
- **`main(self)`**:
  - Prompts the user to select a hash algorithm.
  - Calls the `pair` method with the entered hash and hash type.
- **`pair(self, resolvehash, hash_type)`**:
  - Opens the password dictionary file.
  - Reads each line, converts it to the corresponding hash using the selected algorithm, and compares it with the entered hash.
  - If a match is found, prints the corresponding password and the hash type used.
  - If no match is found, prints a message indicating so.

## Contribution

If you wish to contribute to this project, please follow these steps:

1. Fork the project.
2. Create a branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact [sebacaceresino@gmail.com](sebacaceresino@gmail.com).

