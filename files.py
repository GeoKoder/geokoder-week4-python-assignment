def process_file():
    # Ask user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Open the file and read its content
        with open(filename, 'r') as file:
            content = file.readlines()

        # Modify the content - here we convert it to uppercase
        modified_content = [line.upper() for line in content]

        # Define the name for the new output file
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"File has been read and modified successfully.")
        print(f"Modified content written to: {new_filename}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: The file could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_file()
