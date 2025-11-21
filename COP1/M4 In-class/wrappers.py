'''
Felix Chang
M4 pattern.py
9/11/2025
'''

def main():
    money = int(input("How much money do you have: "))
    bar_count = 0

    for i in range(money // 4):
        bar_count += 1
        if bar_count % 3 == 0:
            bar_count += 1

    print(f"You can purchase {bar_count} candy bars!")

main()