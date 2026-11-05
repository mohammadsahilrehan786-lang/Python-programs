# Manufacturing Cost and Profitability Analysis

material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter total selling price: "))
target = float(input("Enter profit target: "))

# Calculate total production cost
total_cost = material + labour + wastage + machine

# Calculate profit
profit = selling - total_cost

# Display results
print("\n--- Manufacturing Report ---")
print("Material Cost:", material)
print("Labour Charges:", labour)
print("Wastage Cost:", wastage)
print("Machine Cost:", machine)
print("Total Cost:", total_cost)
print("Selling Price:", selling)
print("Profit:", profit)

# Check profit target
if profit >= target:
    print("Profit target achieved!")
else:
    print("Profit target not achieved.")

print("----------------------------")