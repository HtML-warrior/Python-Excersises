def generate_pattern(rows):
    for i in range(rows, 0, -1):
        print("# " * i)

if __name__ == "__main__":
    generate_pattern(8)
