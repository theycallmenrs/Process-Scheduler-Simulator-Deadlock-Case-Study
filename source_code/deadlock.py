# --------------------------------------
# Deadlock Detection using Banker's Algorithm
# --------------------------------------

def is_safe_state(n, m, available, max_need, allocation):
    # Calculate Need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        allocated = False

        for i in range(n):
            if not finish[i]:
                # Check if process can be satisfied
                if all(need[i][j] <= available[j] for j in range(m)):
                    # Allocate resources
                    for j in range(m):
                        available[j] += allocation[i][j]

                    finish[i] = True
                    safe_sequence.append(f"P{i}")
                    allocated = True

        if not allocated:
            return False, []

    return True, safe_sequence


# ----------------------
# MAIN PROGRAM
# ----------------------
def main():
    print("\n--- Deadlock Detection using Banker's Algorithm ---")

    # Number of processes and resources
    n = 3   # processes
    m = 3   # resource types

    # Available resources
    available = [3, 3, 2]

    # Maximum resources needed by each process
    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2]
    ]

    # Resources currently allocated
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2]
    ]

    safe, sequence = is_safe_state(n, m, available.copy(), max_need, allocation)

    if safe:
        print("System is in a SAFE state.")
        print("Safe Sequence:", " -> ".join(sequence))
    else:
        print("DEADLOCK detected! No safe sequence exists.")


if __name__ == "__main__":
    main()
