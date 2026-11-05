# Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

# Calculate gross salary
gross = basic + allowances + overtime + incentives

# Calculate progressive deductions
if gross <= 10000:
    tax = gross * 0.05
elif gross <= 20000:
    tax = 10000 * 0.05 + (gross - 10000) * 0.10
else:
    tax = 10000 * 0.05 + 10000 * 0.10 + (gross - 20000) * 0.15

# Calculate net salary
net = gross - tax

# Print salary statement
print("\n------ SALARY STATEMENT ------")
print("Employee Name :", name)
print("Basic Salary  :", basic)
print("Allowances    :", allowances)
print("Overtime Pay  :", overtime)
print("Incentives    :", incentives)
print("Gross Salary  :", gross)
print("Deduction     :", tax)
print("Net Salary    :", net)
print("------------------------------")