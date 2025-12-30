# Shortest Job First (SJF) Non-Preemptive Scheduler - Python
# This program reads process data from CSV, calculates waiting time, turnaround time,
# and generates a Gantt chart for SJF scheduling.

import csv
<<<<<<< HEAD

# Mapping of choices to CSV file paths
csv_options = {
    1: "csv_test_files/SJF_INPUTS/sjf_input.csv",
    2: "csv_test_files/SJF_INPUTS/sjf_input2.csv",
    3: "csv_test_files/SJF_INPUTS/sjf.input3.csv",
    4: "csv_test_files/SJF_INPUTS/sjf.input4.csv"
}
=======
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
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
# MAIN LOOP - allow user to run multiple CSVs
while True:
    print("\nSelect a CSV file to run (1-4) or 0 to exit:")
    for opt in csv_options:
        print("Choice", opt, ":", csv_options[opt])
    print("0: Exit program")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting program. Goodbye!")
            break
        elif choice in csv_options:
            csv_file = csv_options[choice]
        else:
            print("Invalid choice. Enter 0-4.")
            continue
    except ValueError:
        print("Please enter a valid integer.")
        continue
=======
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
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
    # Step 1: Reading CSV and storing processes
    processes = []
=======

# SJF Scheduling Algorithm
def sjf_scheduling(processes):
    time = 0                    # Current CPU time
    completed = []              # Completed processes
    gantt_chart = []            # Stores Gantt chart info
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append({
                "ProcessId": row["ProcessId"],
                "Arrival_Time": int(row["Arrival_Time"]),
                "Burst_Time": int(row["Burst_Time"])
            })
=======
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
    print("\nInput Processes:")
    print("************************************")
    for P in processes:
        print("Process ID:", P["ProcessId"])
        print("Arrival Time:", P["Arrival_Time"])
        print("Burst Time:", P["Burst_Time"])
        print("********************************")
=======
    while processes:
        # Get all processes that have arrived
        available = [p for p in processes if p.arrival_time <= time]
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
    # Step 2: SJF Scheduling
    # Sort by Arrival Time initially
    processes.sort(key=lambda x: x["Arrival_Time"])
=======
        # If no process is available, CPU remains idle
        if not available:
            time += 1
            continue
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
    completed = 0       # Number of processes completed
    current_time = 0    # Keeps track of CPU time
    n = len(processes)
    is_completed = [False] * n  # Track completed processes
=======
        # Select process with the shortest burst time
        current = min(available, key=lambda x: x.burst_time)
        processes.remove(current)
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

    while completed < n:
        # Find process with shortest burst time among arrived processes
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if processes[i]["Arrival_Time"] <= current_time and not is_completed[i]:
                if processes[i]["Burst_Time"] < min_burst:
                    min_burst = processes[i]["Burst_Time"]
                    idx = i
                # If burst times are equal, choose the one with earlier arrival
                elif processes[i]["Burst_Time"] == min_burst:
                    if processes[i]["Arrival_Time"] < processes[idx]["Arrival_Time"]:
                        idx = i
        
        if idx == -1:  # If no process has arrived yet, increment time
            current_time += 1
            continue

<<<<<<< HEAD
        # Schedule the chosen process
        processes[idx]["start"] = current_time
        processes[idx]["completion"] = processes[idx]["start"] + processes[idx]["Burst_Time"]
        processes[idx]["TAT"] = processes[idx]["completion"] - processes[idx]["Arrival_Time"]
        processes[idx]["WT"] = processes[idx]["TAT"] - processes[idx]["Burst_Time"]
=======
        # Calculate Waiting Time
        current.waiting_time = start_time - current.arrival_time

        # Calculate Turnaround Time
        current.turnaround_time = current.waiting_time + current.burst_time
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
        # Update time and completion
        current_time = processes[idx]["completion"]
        is_completed[idx] = True
        completed += 1
=======
        completed.append(current)

        # Save process execution for Gantt Chart
        gantt_chart.append((current.pid, start_time, end_time))
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

    # Step 3: Calculate average TAT and WT
    total_TAT = sum(p["TAT"] for p in processes)
    total_WT = sum(p["WT"] for p in processes)
    avg_TAT = total_TAT / n
    avg_WT = total_WT / n

    # Step 4: Print results
    print("\n--------------------------------------")
    print("SJF Scheduling Results")
    print("--------------------------------------")

<<<<<<< HEAD
    for P in processes:
        print("Process ID:", P["ProcessId"])
        print("Arrival Time:", P["Arrival_Time"])
        print("Burst Time:", P["Burst_Time"])
        print("Start Time:", P["start"])
        print("Completion Time:", P["completion"])
        print("Turnaround Time(TAT):", P["TAT"])
        print("Waiting Time(WT):", P["WT"])
        print("------------------------------------")
=======
    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")

    # Display each process details
    for p in processes:
        print(f"P{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}")

        # Add times for average calculation
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
    print("Average TAT and WT")
    print("------------------------------------------")
    print("Average Turnaround Time(TAT):", avg_TAT)
    print("Average Waiting Time(WT):", avg_WT)
    print("------------------------------------------")
=======
    # Average Waiting Time Calculation
    avg_waiting_time = total_waiting_time / len(processes)

    # Average Turnaround Time Calculation
    avg_turnaround_time = total_turnaround_time / len(processes)
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

    # Step 5: Gantt Chart
    print("\nGANTT CHART")
    print("=================")

<<<<<<< HEAD
    for P in processes:
        print("|", P["ProcessId"], end=" ")
=======
   
    # Display Text-Based Gantt Chart
    print("\nGantt Chart:")

    # Print process blocks
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ", end="")
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9
    print("|")

<<<<<<< HEAD
    # Printing timeline
    time_marker = 0
    print(time_marker, end=" ")
    for P in processes:
        spaces = 3
        time_marker = P["completion"]
        print(" " * spaces, time_marker, end="")
    print("\n--------------------------------------------")
    print("SJF run completed. You can select another CSV or exit.")
    print("--------------------------------------------\n")
=======
    # Print time line
    print(gantt_chart[0][1], end="")
    for _, _, end in gantt_chart:
        print(f"\t{end}", end="")
    print()
>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9

<<<<<<< HEAD
=======

# Main Program
if __name__ == "__main__":

# Input CSV file
    filename = "sjf_input.csv"    
    process_list = read_processes_from_csv(filename)

    completed_processes, gantt = sjf_scheduling(process_list)
    display_results(completed_processes, gantt)

>>>>>>> 8baf6ed2efade7100565564ba230d021f4620eb9