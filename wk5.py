def read_and_modify_file():
    # ask the user for a filename
    filename=input("Enter the name of the file to read: ")
    try:
        # try to open and read the file
        with open(filename, 'r')as file:
            content = file.read()
            # modify the content(E.g , convert to uppercase)
        modified_content = content.upper()

        # create a new filename to write the modified content
        new_filename = f"modified_{filename}"
        # write the modified content to the new file
        with open(new_filename, 'w')as file:
            file.write(modified_content)

            print(f"modified content written to '{new_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read or written.")
# run the function
read_and_modify_file()
