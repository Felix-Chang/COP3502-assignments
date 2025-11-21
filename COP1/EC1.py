total_price = 0

print("Available movies today:")

print("A)12 Strong:\t1)2:30\t2)4:40\t3)7:50\t4)10:50")
print("B)Coco:\t1)12:40\t2)3:45")
print("C)The Post:\t1)12:45\t2)3:35\t3)7:05\t4)9:55")

choice = input("Movie choice:\t")

if choice == "A":
    time = input("Showtime:\t")

    if time == "1" or time == "2":
        adult_tickets = int(input("Adult tickets:\t"))
        kid_tickets = int(input("Kid tickets:\t"))
    
        if (kid_tickets + adult_tickets) > 30:
            print("Invalid option; please restart app...")
        else: 
            total_price += (kid_tickets * 9.68 + adult_tickets * 12.45)
            print(f"Total cost:\t${total_price:.2f}")

    elif time == "3" or time == "4":
        adult_tickets = int(input("Adult tickets:\t"))
        kid_tickets = int(input("Kid tickets:\t"))
        
        if (kid_tickets + adult_tickets) > 30:
            print("Invalid option; please restart app...")
        else: 
            total_price += (kid_tickets * 9.68 + adult_tickets * 12.45)
            print(f"Total cost:\t${total_price:.2f}")
    else:
        print("Invalid option; please restart app...")

elif choice == "B":
    time = input("Showtime:\t")

    if time == "1":
        adult_tickets = int(input("Adult tickets:\t"))
        kid_tickets = int(input("Kid tickets:\t"))

        if (kid_tickets + adult_tickets) > 30:
            print("Invalid option; please restart app...")
        else: 
            total_price += (kid_tickets * 8 + adult_tickets * 11.17)
            print(f"Total cost:\t${total_price:.2f}")

    elif time == "2":
        adult_tickets = int(input("Adult tickets:\t"))
        kid_tickets = int(input("Kid tickets:\t"))

        if (kid_tickets + adult_tickets) > 30:
            print("Invalid option; please restart app...")
        else: 
            total_price += (kid_tickets * 9.68 + adult_tickets * 12.45)
            print(f"Total cost:\t${total_price:.2f}")
    else:
        print("Invalid option; please restart app...")

elif choice == "C":
    time = input("Showtime:\t")

    if time == "1":
        adult_tickets = int(input("Adult tickets:\t"))
        kid_tickets = int(input("Kid tickets:\t"))

        if (kid_tickets + adult_tickets) > 30:
            print("Invalid option; please restart app...")
        else: 
            total_price += (kid_tickets * 8 + adult_tickets * 11.17)
            print(f"Total cost:\t${total_price:.2f}")

    elif time == "2" or time == "3" or time == "4":
        adult_tickets = int(input("Adult tickets:\t"))
        kid_tickets = int(input("Kid tickets:\t"))

        if (kid_tickets + adult_tickets) > 30:
            print("Invalid option; please restart app...")
        else: 
            total_price += (kid_tickets * 9.68 + adult_tickets * 12.45)
            print(f"Total cost:\t${total_price:.2f}")
    else:
        print("Invalid option; please restart app...")

else:
    print("Invalid option; please restart app...")