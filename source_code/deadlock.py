import pandas as pd

# PART 1: CPU Scheduler Simulator
def round_robin(processes, quantum):
    n = len(processes)
    remaining_bt = list(processes['BurstTime'])
    time = 0
    gantt_chart = []
    waiting_time = [0]*n
    turnaround_time = [0]*n

    # Execution loop
    while sum(remaining_bt) > 0:
        for i in range(n):
            if remaining_bt[i] > 0:
                exec_time = min(quantum, remaining_bt[i])
                gantt_chart.append((processes['ProcessID'][i], time, time+exec_time))
                time += exec_time
                remaining_bt[i] -= exec_time

    # Calculate WT and TAT
    for i in range(n):
        turnaround_time[i] = time - processes['ArrivalTime'][i]
        waiting_time[i] = turnaround_time[i] - processes['BurstTime'][i]

    avg_wt = sum(waiting_time)/n
    avg_tat = sum(turnaround_time)/n

    return gantt_chart, waiting_time, turnaround_time, avg_wt, avg_tat

# PART 2: Deadlock Detection (Banker’s)

def is_safe(n, m, available, max_d, allocation):
    need = [[max_d[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False]*n
    safe_seq = []

    while len(safe_seq) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= available[j] for j in range(m)):
                for j in range(m):
                    available[j] += allocation[i][j]
                finish[i] = True
                safe_seq.append(i)
                allocated = True
        if not allocated:
            return False, []
    return True, safe_seq


# MAIN PROGRAM

def main():
    print("\n--- CPU Scheduler Simulator (Round Robin) ---")
    # Example process data (can also read from CSV)
    data = {'ProcessID': ['P1', 'P2', 'P3'],
            'ArrivalTime': [0, 0, 0],
            'BurstTime': [10, 5, 8]}
    processes = pd.DataFrame(data)
    quantum = 3

    gantt, wt, tat, avg_wt, avg_tat = round_robin(processes, quantum)

    print("\nGantt Chart (Process, Start, End):")
    for entry in gantt:
        print(entry)

    print("\nWaiting Times:", wt)
    print("Turnaround Times:", tat)
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


    # Deadlock Detection
    print("\n--- Deadlock Detection (Banker's Algorithm) ---")

    # Example data
    n = 3  # processes
    m = 3  # resources
    available = [3, 3, 2]
    max_d = [[7,5,3], [3,2,2], [9,0,2]]
    allocation = [[0,1,0], [2,0,0], [3,0,2]]

    safe, sequence = is_safe(n, m, available.copy(), max_d, allocation)

    if safe:
        print("System is in a SAFE state.")
        print("Safe sequence of execution (process indices):", sequence)
    else:
        print("DEADLOCK detected! No safe sequence exists.")

    
    # Real-World Deadlock Case Study
    
    print("\n--- Real-World Deadlock Case Study: Database Deadlock ---")
    print("""
Scenario:
- Two users try to update bank accounts simultaneously.
- User A locks Account 1, User B locks Account 2.
- Both try to access the other's account, causing a deadlock.

Causes:
- Mutual exclusion (resource can be used by one process at a time)
- Hold and wait (process holds one resource and waits for another)
- No preemption (resources can't be forcibly taken)
- Circular wait (each process waits for another in a circle)

Prevention:
1. Resource ordering (always acquire locks in same order)
2. Timeouts (abort if waiting too long)
3. Deadlock detection (Banker's Algorithm)
4. Avoid circular wait (break one of the four conditions)
""")

if __name__ == "__main__":
    main()
