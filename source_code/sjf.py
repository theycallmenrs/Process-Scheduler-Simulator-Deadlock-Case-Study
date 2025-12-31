import csv

# Process class
# Process class represents a single process in CPU scheduling
#part 1
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid                  # Process ID (unique identifier)
        self.arrival_time = arrival_time  # Time when process enters ready queue
        self.burst_time = burst_time      # CPU time required by the process

        # These will be calculated during scheduling
        self.waiting_time = 0            # Time process waits in ready queue
        self.turnaround_time = 0         # Total time from arrival to completion
# ==========================
# Program Entry Point
# ==========================
if __name__ == "__main__":
    main()

# Read CSV file
#part 2
def read_csv(file_path):
    """
    Reads process data from a CSV file and returns
    a list of Process objects.
    """
    processes = []

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Create Process object from CSV row
                process = Process(
                    int(row['pid']),                 # Convert PID to integer
                    int(row['arrival_time']),        # Arrival time
                    int(row['burst_time'])           # Burst time
                )
                processes.append(process)

    except FileNotFoundError:
        print("ERROR: CSV file not found!")
        exit()

    except KeyError:
        print("ERROR: CSV file format is incorrect!")
        exit()

    return processes
# ==========================
# Program Entry Point
# ==========================
if __name__ == "__main__":
    main()=


#part 3
# SJF Scheduling (Non-preemptive)
def sjf_scheduling(processes):
    """
    Performs Non-Preemptive Shortest Job First scheduling.
    Returns completed processes and Gantt chart.
    """

    time = 0                    # Current CPU time
    completed = []               # List of completed processes
    gantt_chart = []             # Stores execution order for visualization

    # Sort processes by arrival time first
    processes.sort(key=lambda p: p.arrival_time)

    while processes:
        # Select processes that have already arrived
        available_processes = [
            p for p in processes if p.arrival_time <= time
        ]

        # If no process is available, CPU is idle
        if not available_processes:
            gantt_chart.append(("IDLE", time, time + 1))
            time += 1
            continue

        # Choose process with the shortest burst time
        current_process = min(
            available_processes,
            key=lambda p: p.burst_time
        )

        processes.remove(current_process)

        start_time = time
        time += current_process.burst_time
        end_time = time

        # Calculate waiting and turnaround times
        current_process.waiting_time = start_time - current_process.arrival_time
        current_process.turnaround_time = (
            current_process.waiting_time + current_process.burst_time
        )

        # Save results
        completed.append(current_process)
        gantt_chart.append(
            (current_process.pid, start_time, end_time)
        )

    return completed, gantt_chart
# ==========================
# Program Entry Point
# ==========================
if __name__ == "__main__":
    main()


#part 4 # Display results
def display_results(processes, gantt_chart):
    """
    Displays waiting time, turnaround time,
    averages and Gantt chart.
    """

    total_waiting_time = 0
    total_turnaround_time = 0

    print("\nPROCESS SCHEDULING RESULTS")
    print("--------------------------------------")
    print("PID | Arrival | Burst | Waiting | Turnaround")
    print("--------------------------------------")

    # Sort processes by PID for neat output
    processes.sort(key=lambda p: p.pid)

    for p in processes:
        print(
            f"{p.pid:3} |"
            f"{p.arrival_time:8} |"
            f"{p.burst_time:6} |"
            f"{p.waiting_time:7} |"
            f"{p.turnaround_time:10}"
        )
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time

    n = len(processes)

    print("--------------------------------------")
    print("Average Waiting Time   =", total_waiting_time / n)
    print("Average Turnaround Time =", total_turnaround_time / n)

    print("\nGANTT CHART:")
    for item in gantt_chart:
        pid, start, end = item
        print(f"| {pid} ({start}-{end}) ", end="")
    print("|")
   # ==========================
# Program Entry Point
# ==========================
if __name__ == "__main__":
    main()

    
#part5 # Main
def main():
    csv_options = {
        1: "csv_test_files/SJF_INPUTS/sjf_input_case1.csv",
        2: "csv_test_files/SJF_INPUTS/sjf_input_case2.csv",
        3: "csv_test_files/SJF_INPUTS/sjf_input_case3.csv",
        4: "csv_test_files/SJF_INPUTS/sjf_input_case4.csv"
    }

    while True:
        print("\nCHOOSE CSV FILE (Enter 0 to exit):")
        for k, v in csv_options.items():
            print(f"{k}. {v}")
        print("0. Exit program")

        # Input validation loop
        try:
            choice = int(input("Enter choice (0-4): "))

            if choice == 0:
                print("Exiting program. Goodbye!")
                break  # Exit the while loop -> program ends

            if choice in csv_options:
                processes = read_csv(csv_options[choice])
                completed, gantt = sjf_scheduling(processes)
                display_results(completed, gantt)
            else:
                print("Invalid choice! Please select a number between 0 and 4.")

        except ValueError:
            print("Invalid input! Please enter a number between 0 and 4.")
    
# ==========================
# Program Entry Point
# ==========================
if __name__ == "__main__":
    main()