"""
Deadlock Detection using Banker's Algorithm
"""

# Number of processes and resources
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

# Input Allocation Matrix
print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    allocation.append(list(map(int, input(f"P{i}: ").split())))

# Input Maximum Matrix
print("\nEnter Maximum Matrix:")
max_need = []
for i in range(n):
    max_need.append(list(map(int, input(f"P{i}: ").split())))

# Input Available Resources
available = list(map(int, input("\nEnter Available Resources: ").split()))

# Calculate Need Matrix
need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

print("\nNeed Matrix:")
for i in range(n):
    print(f"P{i}:", need[i])

# Banker's Algorithm
finish = [False] * n
safe_sequence = []
work = available.copy()

while len(safe_sequence) < n:
    found = False
    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(m)):
                # Process can execute
                for j in range(m):
                    work[j] += allocation[i][j]
                safe_sequence.append(f"P{i}")
                finish[i] = True
                found = True
    if not found:
        break

# Output result
if len(safe_sequence) == n:
    print("\nSystem is in a SAFE state")
    print("Safe Sequence:", " -> ".join(safe_sequence))
else:
    print("\nDEADLOCK DETECTED!")
    print("System is in an UNSAFE state")
