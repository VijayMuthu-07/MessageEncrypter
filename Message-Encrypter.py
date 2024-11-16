import string
import random
char=string.ascii_letters+string.digits+string.punctuation+" "
char=list(char)
key=char.copy()
random.shuffle(key)

def main():
    message=""

    print("Welcome")
    print("1.Encode")
    print("2.Decode")
    print("3.Exit")
    while True:
        choice=input("Enter your choice: ")
        if not choice.isdigit():
            continue
        choice=int(choice)

        if choice==1:
            message=encode(char,key)
            print("Your encrypted message is: ")
            print(message)
        elif choice==2:
            message=decode(char,key)
            print("Your decrypted message is: ")
            print(message)
        else:
            print("Thank You")
            break

def encode(l,k):
    code=""
    mess=input("Enter the message: ")
    for ele in mess:
        i=l.index(ele)
        code=code+k[i]
    return code

def decode(l,k):
    code=""
    mess=input("enter your message: ")
    for ele in mess:
        i=k.index(ele)
        code=code+l[i]
    return code

if __name__=="__main__":
    main()