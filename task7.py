# Monthly Calendar Generator

start = int(input("Enter starting weekday (0=Sun, 1=Mon, ..., 6=Sat): "))
days = int(input("Enter number of days in month: "))

if start < 0 or start > 6 or days < 28 or days > 31:
    print("Invalid input!")
else:
    print("\nSun Mon Tue Wed Thu Fri Sat")

    for i in range(start):
        print("    ", end="")

    for day in range(1, days + 1):
        print(f"{day:3}", end="  ")

        if (start + day) % 7 == 0:
            print()

    print()