import console_gfx

def display_menu():
    print("\nRLE Menu\n"
          "--------\n"
          "0. Exit\n"
          "1. Load File\n"
          "2. Load Test Image\n"
          "3. Read RLE String\n"
          "4. Read RLE Hex String\n"
          "5. Read Data Hex String\n"
          "6. Display Image\n"
          "7. Display RLE String\n"
          "8. Display Hex RLE Data\n"
          "9. Display Hex Flat Data\n")

def main():
    print("Welcome to the RLE image encoder!\n\n"
                   "Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)

    while True:
        display_menu()
        option = int(input("\nSelect a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_name)
        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif option == 3:
            image_data = input("Enter an RLE string to be decoded: ")
        elif option == 4:
            image_data = input("Enter the hex string holding RLE data: ")
        elif option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data)


if __name__ == "__main__":
    main()