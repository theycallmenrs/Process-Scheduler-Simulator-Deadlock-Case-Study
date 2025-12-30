"""
Process Scheduler Simulator - SJF (Non-Preemptive)
This program simulates the Shortest Job First (SJF) CPU scheduling algorithm.
It:
1. Calculates Waiting Time for each process
2. Calculates Turnaround Time for each process
3. Calculates Average Waiting Time
4. Calculates Average Turnaround Time
5. Displays a text-based Gantt Chart
"""

import csv
# Process class
# Stores process details
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid                    
        # Process ID
        self.arrival_time = arrival_time   
        # Arrival Time
        self.burst_time = burst_time      
        # CPU Burst Time
        self.waiting_time = 0              
        # Waiting Time
        self.turnaround_time = 0          
        # Turnaround Time

# Read process data from CSV file
def read_processes_from_csv(filename):
    processes = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create Process object from CSV values
            processes.append(
                Process(
                    int(row['pid']),
                    int(row['arrival_time']),
                    int(row['burst_time'])
                )
            )
    return processes


# SJF Scheduling Algorithm
def sjf_scheduling(processes):
    time = 0                    # Current CPU time
    completed = []              # Completed processes
    gantt_chart = []            # Stores Gantt chart info

    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    while processes:
        # Get all processes that have arrived
        available = [p for p in processes if p.arrival_time <= time]

        # If no process is available, CPU remains idle
        if not available:
            time += 1
            continue

        # Select process with the shortest burst time
        current = min(available, key=lambda x: x.burst_time)
        processes.remove(current)

        start_time = time
        time += current.burst_time
        end_time = time

        # Calculate Waiting Time
        current.waiting_time = start_time - current.arrival_time

        # Calculate Turnaround Time
        current.turnaround_time = current.waiting_time + current.burst_time

        completed.append(current)

        # Save process execution for Gantt Chart
        gantt_chart.append((current.pid, start_time, end_time))

    return completed, gantt_chart

# Display Results
def display_results(processes, gantt_chart):
    total_waiting_time = 0
    total_turnaround_time = 0

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")

    # Display each process details
    for p in processes:
        print(f"P{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}")

        # Add times for average calculation
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time

    # Average Waiting Time Calculation
    avg_waiting_time = total_waiting_time / len(processes)

    # Average Turnaround Time Calculation
    avg_turnaround_time = total_turnaround_time / len(processes)

    print("\nAverage Waiting Time =", avg_waiting_time)
    print("Average Turnaround Time =", avg_turnaround_time)

   
    # Display Text-Based Gantt Chart
    print("\nGantt Chart:")

    # Print process blocks
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ", end="")
    print("|")

    # Print time line
    print(gantt_chart[0][1], end="")
    for _, _, end in gantt_chart:
        print(f"\t{end}", end="")
    print()


# Main Program
if __name__ == "__main__":

# Input CSV file
    filename = "sjf_input.csv"    
    process_list = read_processes_from_csv(filename)

    completed_processes, gantt = sjf_scheduling(process_list)
    display_results(completed_processes, gantt)
