from datetime import datetime

# Parking Fee Management

entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

try:
    start = datetime.strptime(entry, "%H:%M")
    end = datetime.strptime(exit_time, "%H:%M")

    if start == end:
        raise ValueError("Entry and exit times cannot be the same.")

    if end < start:
        end = end.replace(day=2)

    hours = (end - start).seconds / 3600
    hours = int(hours) if hours == int(hours) else int(hours) + 1

    vehicle = input("Enter vehicle type (car/bike): ").lower()

    if vehicle == "car":
        rate = 30
    elif vehicle == "bike":
        rate = 15
    else:
        print("Invalid vehicle type!")
        exit()

    fee = hours * rate

    # Overnight parking charge
    if end.date() != start.date():
        fee += 100

    # Daily maximum limit
    fee = min(fee, 300)

    # Penalty for parking over 24 hours
    if hours > 24:
        fee += 200

    print("\n--- Parking Receipt ---")
    print("Vehicle Type:", vehicle)
    print("Parking Hours:", hours)
    print("Parking Fee: Rs.", fee)

except ValueError:
    print("Invalid time! Enter time in HH:MM format.")