"""
Process Scheduler Simulator - SJF (Non-Preemptive)

This program simulates the Shortest Job First (SJF) CPU scheduling algorithm.
It calculates:
1. Waiting Time
2. Turnaround Time
3. Displays a text-based Gantt Chart

Author: Neelam
"""
# -----------------------------
# Process class to store details
# -----------------------------
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


# ---------------------------------
# SJF Scheduling Function
# ---------------------------------
def sjf_scheduling(processes):
    time = 0
    completed = []
    gantt_chart = []

    # Sort processes by arrival time first
    processes.sort(key=lambda x: x.arrival_time)

    while processes:
        # Get all processes that have arrived
        available = [p for p in processes if p.arrival_time <= time]

        if not available:
            time += 1
       continue

        # Select process with shortest burst time
        current = min(available, key=lambda x: x.burst_time)

        processes.remove(current)

        start_time = time
        time += current.burst_time
        end_time = time

        # Calculate waiting and turnaround time
        current.waiting_time = start_time - current.arrival_time
        current.turnaround_time = current.waiting_time + current.burst_time

        completed.append(current)
        gantt_chart.append((current.pid, start_time, end_time))

    return completed, gantt_chart


# ---------------------------------
# Display Results
# ---------------------------------
def display_results(processes, gantt_chart):
    total_wt = 0
    total_tat = 0

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
    for p in processes:
        print(f"P{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}")
        total_wt += p.waiting_time
        total_tat += p.turnaround_time

    print("\nAverage Waiting Time:", total_wt / len(processes))
    print("Average Turnaround Time:", total_tat / len(processes))

    # Gantt Chart
    print("\nGantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ", end="")
    print("|")

    print(gantt_chart[0][1], end="")
    for _, _, end in gantt_chart:
        print(f"\t{end}", end="")
    print()


# ---------------------------------
# Main Program
# ---------------------------------
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    process_list = []

    for i in range(n):
        at = int(input(f"Enter arrival time of P{i + 1}: "))
        bt = int(input(f"Enter burst time of P{i + 1}: "))
        process_list.append(Process(i + 1, at, bt))

    completed_processes, gantt = sjf_scheduling(process_list)
    display_results(completed_processes, gantt)
