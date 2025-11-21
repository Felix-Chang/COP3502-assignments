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

def to_hex_string(data):
    hex_string = ""
    for x in data:
        if x < 10:
            hex_string += str(x)
        elif x == 10:
            hex_string += "a"
        elif x == 11:
            hex_string += "b"
        elif x == 12:
            hex_string += "c"
        elif x == 13:
            hex_string += "d"
        elif x == 14:
            hex_string += "e"
        elif x == 15:
            hex_string += "f"
    return hex_string

def count_runs(flat_data):
    if not flat_data:
        return 0

    runs = 1
    length = 1

    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i-1] and length < 15:
            length += 1
        else:
            runs += 1
            length = 1
    
    return runs

def encode_rle(flat_data):
    if not flat_data:
        return []
    
    RLE_data = []
    count = 1

    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i-1] and count < 15:
            count += 1
        else:
            RLE_data.extend([count, flat_data[i-1]]) 
            count = 1
    
    RLE_data.extend([count, flat_data[-1]])

    return RLE_data

def get_decoded_length(rle_data):
    length = 0
    for i in range(0, len(rle_data), 2):
        length += rle_data[i]
    return length

def decode_rle(rle_data):
    output = []
    for i in range(0, len(rle_data), 2):
        output.extend(rle_data[i] * [rle_data[i + 1]])
    return output

def string_to_data(data_string):
    rle_data = []
    for i in range(0, len(data_string), 2):
        # convert count to number
        if data_string[i] in "0123456789":
            count = int(data_string[i])
        elif data_string[i] == "a":
            count = 10
        elif data_string[i] == "b":
            count = 11
        elif data_string[i] == "c":
            count = 12
        elif data_string[i] == "d":
            count = 13
        elif data_string[i] == "e":
            count = 14
        elif data_string[i] == "f":
            count = 15
        
        # convert value to number
        if data_string[i+1] in "0123456789":
            value = int(data_string[i+1])
        elif data_string[i+1] == "a":
            value = 10
        elif data_string[i+1] == "b":
            value = 11
        elif data_string[i+1] == "c":
            value = 12
        elif data_string[i+1] == "d":
            value = 13
        elif data_string[i+1] == "e":
            value = 14
        elif data_string[i+1] == "f":
            value = 15

        rle_data.extend([count, value])
        
    return rle_data

def to_rle_string(rle_data):
    output = []
    for i in range(0, len(rle_data), 2):
        length = str(rle_data[i])
        if str(rle_data[i+1]) in "0123456789":
            value = str(rle_data[i+1])
        elif rle_data[i+1] == 10:
            value = "a"
        elif rle_data[i+1] == 11:
            value = "b"
        elif rle_data[i+1] == 12:
            value = "c"
        elif rle_data[i+1] == 13:
            value = "d"
        elif rle_data[i+1] == 14:
            value = "e"
        elif rle_data[i+1] == 15:
            value = "f"

        output.append(length + value)
    
    output = ":".join(output)
    return output

def string_to_rle(rle_string):
    chunks = rle_string.split(":")
    rle_data = []

    for element in chunks:
        if len(element) == 2:
            length = int(element[:1])
        elif len(element) == 3:
            length = int(element[:2])
        
        value = element[-1]
        if str(value) in "0123456789":
            value = int(value)
        elif value == "a":
            value = 10
        elif value == "b":
            value = 11
        elif value == "c":
            value = 12
        elif value == "d":
            value = 13
        elif value == "e":
            value = 14
        elif value == "f":
            value = 15
        rle_data.extend([length, value])
    
    return rle_data


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
            rle_string = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_string))
        elif option == 4:
            rle_hex = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(rle_hex))
        elif option == 5:
            data_hex = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(data_hex)
        elif option == 6:
            print("Displaying image...")
            if not image_data:
                print("(no data)")
            else:
                console_gfx.display_image(image_data)
        elif option == 7:
            print(f"RLE representation: {to_rle_string(encode_rle(image_data))}")
        elif option == 8:
            print(f"RLE hex values: {to_hex_string(encode_rle(image_data))}")
        elif option == 9:
            print(f"Flat hex values: {to_hex_string(image_data)}")
        else:
            print("Error! Invalid input.")
        
if __name__ == "__main__":
    main()