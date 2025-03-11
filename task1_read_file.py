# Task 1: Read a File and Handle Errors

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print("Reading file content:")
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    file_name = "sample.txt"
    read_file(file_name)