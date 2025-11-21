'''
Felix Chang
M4 pattern.py
9/11/2025
'''

def main():
    height = int(input("Height: "))

    for i in range(1, height + 1):
        print(" " * (height - i), end = "")

        for j in range(1, i + 1):
            print(j, end = "")
        print()
            
main()