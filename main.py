
#new push

def encode(num):
    encoded_password = ""
    for char in num:

        new_digit = (int(char) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password

def decode(encoded_password):
    original_password = ""
    for digit in encoded_password:
        original_digit = str((int(digit) - 3) % 10)  # Shift the digit down by 3 and handle wrap-around
        original_password += original_digit

    return original_password


if __name__=="__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option"))
        if option == 1:
            num = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
        if option == 2:
            print(f"The encoded password is {encode(num)}, and the original password is {num}")
        if option == 3:
            break


