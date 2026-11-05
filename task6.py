# Repeated Transaction Detection

transactions = [
    ("T101", 500),
    ("T102", 2000),
    ("T101", 500),
    ("T103", 15000),
    ("T104", 3000)
]

seen = set()
suspicious = []

threshold = 10000

for tid, amount in transactions:
    if tid in seen or amount > threshold:
        suspicious.append((tid, amount))

    seen.add(tid)

print("--- Transaction Report ---")

print("All Transactions:")
for tid, amount in transactions:
    print(tid, ":", amount)

print("\nSuspicious Transactions:")
for tid, amount in suspicious:
    print(tid, ":", amount)

print("\nTotal Suspicious Entries:", len(suspicious))