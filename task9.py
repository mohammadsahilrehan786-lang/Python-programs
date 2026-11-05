# Bus Passenger Occupancy Simulation

capacity = int(input("Enter bus capacity: "))
passengers = 0
stops = int(input("Enter number of stops: "))

for i in range(1, stops + 1):
    print("\nStop", i)
    boarding = int(input("Enter boarding passengers: "))
    alighting = int(input("Enter alighting passengers: "))

    if boarding < 0 or alighting < 0 or alighting > passengers:
        print("Invalid passenger count!")
        continue

    passengers = passengers - alighting + boarding

    print("Passengers in bus:", passengers)

    if passengers > capacity:
        print("Capacity violation!")
    else:
        print("Within capacity.")

print("\nFinal passengers:", passengers)