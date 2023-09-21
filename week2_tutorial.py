def find_smallest_largest(num1, num2, num3):
    smallest = min(num1, num2, num3)
    largest = max(num1, num2, num3)
    return smallest, largest

if __name__ == "__main__":
    try:
        input_numbers = input("Enter the three numbers separated by commas: ")
        num_list = [int(num) for num in input_numbers.split(",")]

        if len(num_list) != 3:
            print("Please enter exactly three numbers separated by commas.")
        else:
            smallest, largest = find_smallest_largest(*num_list)
            print(f"Largest: {largest} Smallest: {smallest}")
    except ValueError:
        print("Invalid input. Please enter valid integer numbers separated by commas.")
