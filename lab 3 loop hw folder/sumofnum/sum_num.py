def main():
    sum_of_numbers = 0

    while True:
        user_input = float(input("Enter a positive number (or a negative number to exit): "))

        if user_input < 0:
            break
        else:
            sum_of_numbers += user_input

    print(f"\nSum of all the numbers entered: {sum_of_numbers}")

if __name__ == "__main__":
    main()
