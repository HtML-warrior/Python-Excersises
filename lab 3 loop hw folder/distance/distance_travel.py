def calculate_distance(speed, time):
    print("\nHour\tDistance Travelled")
    print("------------------------")

    for hour in range(1, time + 1):
        distance = speed * hour
        print(f"{hour}\t{distance}")

if __name__ == "__main__":
    speed = float(input("Enter the speed of the vehicle (mph): "))
    time = int(input("Enter the hours travelled: "))

    calculate_distance(speed, time)
