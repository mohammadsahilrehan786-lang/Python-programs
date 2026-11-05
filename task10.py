# Retail Order Dispatch and Return Analysis

inventory = int(input("Enter available inventory: "))
ordered = int(input("Enter order quantity: "))
dispatched = int(input("Enter dispatched quantity: "))
returned = int(input("Enter returned quantity: "))

# Validate records
if inventory < 0 or ordered < 0 or dispatched < 0 or returned < 0:
    print("Invalid quantities!")

elif dispatched > ordered or returned > dispatched:
    print("Inconsistent records!")

else:
    # Calculate outstanding orders
    outstanding = ordered - dispatched

    # Update inventory
    inventory = inventory - dispatched + returned

    # Display report
    print("\n--- Retail Order Report ---")
    print("Ordered Quantity:", ordered)
    print("Dispatched Quantity:", dispatched)
    print("Returned Quantity:", returned)
    print("Outstanding Orders:", outstanding)
    print("Updated Inventory:", inventory)

    print("Records are consistent.")