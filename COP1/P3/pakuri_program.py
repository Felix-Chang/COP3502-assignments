from pakudex import Pakudex

def main():
    while True:
        print("Welcome to Pakudex: Tracker Extraordinaire!")

        while True:
            try:
                capacity = int(input("Enter max capacity of the Pakudex: "))
                if capacity <= 0:
                    print("Please enter a valid size.")
                    continue
                break
            except ValueError:
                print("Please enter a valid size.")

        my_pakudex = Pakudex(capacity)
        print(f"The Pakudex can hold {capacity} species of Pakuri.\n")

        while True:
            print("Pakudex Main Menu\n"
                "-----------------\n"
                "1. List Pakuri\n"
                "2. Show Pakuri\n"
                "3. Add Pakuri\n"
                "4. Evolve Pakuri\n"
                "5. Sort Pakuri\n"
                "6. Exit\n")
            option = input("What would you like to do? ")

            if option == "1":
                my_pakuris = my_pakudex.get_species_array()
                if not my_pakuris:
                    print("No Pakuri in Pakudex yet!")
                else:
                    print("Pakuri In Pakudex:")
                    for i in range(len(my_pakuris)):
                        print(f"{i+1}. {my_pakuris[i]}")
            
            elif option == "2":
                my_pakuri_name = input("Enter the name of the species to display: \n")
                my_pakuri_stats = my_pakudex.get_stats(my_pakuri_name)
                if not my_pakuri_stats:
                    print("Error: No such Pakuri!")
                else:
                    print(f"Species: {my_pakuri_name}"
                          f"Attack: {my_pakuri_stats[0]}"
                          f"Defense: {my_pakuri_stats[1]}"
                          f"Speed: {my_pakuri_stats[2]}")
            
            elif option == "3":
                if my_pakudex.get_size() >= my_pakudex.get_capacity():
                    print("Error: Pakudex is full!")
                else:
                    my_pakuri_name = input("Enter the name of the species to add: ")
                    if my_pakudex.add_pakuri(my_pakuri_name):
                        print(f"Pakuri species {my_pakuri_name} successfully added!")
                    else:
                        print("Error: Pakudex already contains this species!")

            elif option == "4":
                my_pakuri_name = input("Enter the name of the species to evolve: ")
                if my_pakudex.evolve_species(my_pakuri_name):
                    print(f"{my_pakuri_name} has evolved!")
                else:
                    print("Error: No such Pakuri!")
            
            elif option == "5":
                my_pakudex.sort_pakuri()
                print("Pakuri have been sorted!")

            elif option == "6":
                print("Thanks for using Pakudex! Bye!")
                break
            else:
                print("Unrecognized menu selection!")
        break

main()