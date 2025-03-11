# Task 2: Write and Append Data to a File

def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data + "\n")
        print("Data successfully written to", file_name)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def append_to_file(file_name, data):
    try:
        with open(file_name, 'a') as file:
            file.write(data + "\n")
        print("Data successfully appended.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def read_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            print("Final content of", file_name + ":")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    file_name = "output.txt"

    # Take user input for writing to the file
    initial_data = input("Enter text to write to the file: ")
    write_to_file(file_name, initial_data)

    # Take user input for appending to the file
    additional_data = input("Enter additional text to append: ")
    append_to_file(file_name, additional_data)

    # Display the final content of the file
    read_file_content(file_name)