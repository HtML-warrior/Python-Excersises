def main():
    print("Numbers divisible by 5 or 6 between 1-100:")
    for num in range(1, 101):
        if num % 5 == 0 or num % 6 == 0:
            print(num, end=' ')

    print("\n\nNumbers divisible by 5 and 6 between 1-100:")
    for num in range(1, 101):
        if num % 5 == 0 and num % 6 == 0:
            print(num, end=' ')

if __name__ == "__main__":
    main()
