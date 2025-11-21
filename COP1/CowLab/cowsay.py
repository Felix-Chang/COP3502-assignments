import sys
from heifer_generator import get_cows

def list_cows(cows):
    print("Cows available:", end = "")
    for cow in cows:
        print(f" {cow.get_name()}", end = "")
    print()
    return 

def main():
    cows = get_cows()
    args = sys.argv[1:]

    if args[0] == "-l":
        list_cows(cows)

    elif args[0] == "-n":
        if args[1] == "heifer":
            for word in args[2:]:
                print(word, end = " ")
            print()
            print(cows[0].get_image())
        elif args[1] == "kitteh":
            for word in args[2:]:
                print(word, end = " ")
            print()
            print(cows[1].get_image())
        elif args[1] == "ice-dragon":
            for word in args[2:]:
                print(word, end = " ")
            print()
            print(cows[3].get_image())
            print("This dragon cannot breathe fire.")
        elif args[1] == "dragon":
            for word in args[2:]:
                print(word, end = " ")
            print()
            print(cows[3].get_image())
            print("This dragon can breathe fire.")
        else:
            print(f"Could not find {args[1]} cow!")

    else:
        for word in args[0:]:
            print(word, end = " ")
        print()
        print(cows[0].get_image())
        
main()