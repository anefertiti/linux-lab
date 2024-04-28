import sys

def my_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char.upper()) + shift
            if shifted > ord('Z'):
                shifted -= 26
            result += chr(shifted)
    return result

def main():
    if len(sys.argv) != 2:
        return
    try: 
        shift_amount = int(sys.argv[1])
        if shift_amount <-25 or shift_amount> 25:
            return
    except ValueError:
        return
    message = input().strip().replace(" ", "").upper()
    encoded_message = my_cipher(message, shift_amount)
    
    count = 0
    for char in encoded_message:
        if count == 5:
            print(" ", end="")
            count = 0
        if count == 10:
            print()
            count = 0
        print(char, end="")
        count += 1
    
    print()

if __name__ == "__main__":
    main()

