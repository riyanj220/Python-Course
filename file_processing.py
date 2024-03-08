def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            data = file.readlines()

        numbers = [int(num) for num in data[0].strip().split(',')]

        average = calculate_average(numbers)

        with open(output_filename, 'w') as file:
            file.write(f"Numbers: {numbers}\n")
            file.write(f"Average: {average:.2f}\n")

    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error: Data in the file is not in the expected format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


