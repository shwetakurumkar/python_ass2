def get_positive_integer():
    while True:
        try:
            num = int(input("enter a positive integer: "))
            if num > 0:
                print(f"Correct! You entered a positive integer: {num}")
                break
            else:
                print("Error: The number is not positive.")
        except ValueError:
            print("Error: Invalid input.")

get_positive_integer()