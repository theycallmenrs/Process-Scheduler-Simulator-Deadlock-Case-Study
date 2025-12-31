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


#part 4 # Display results
def display_results(processes, gantt_chart):
    total_waiting = 0
    total_turnaround = 0

    print("\nProcess | Waiting Time | Turnaround Time")
    print("----------------------------------------")

    for p in processes:
        print(f"{p.pid:7} | {p.waiting:12} | {p.turnaround:15}")
        total_waiting += p.waiting
        total_turnaround += p.turnaround

    print("\nAverage Waiting Time:", total_waiting / len(processes))
    print("Average Turnaround Time:", total_turnaround / len(processes))

    print("\nGantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| {pid} ({start}-{end}) ", end="")
    print("|")


#part5 # Main
if __name__ == "__main__":
    csv_options = {
        1: "csv_test_files/SJF_INPUTS/sjf_input.csv",
        2: "csv_test_files/SJF_INPUTS/sjf_input2.csv",
        3: "csv_test_files/SJF_INPUTS/sjf.input3.csv",
        4: "csv_test_files/SJF_INPUTS/sjf.input4.csv"
    }

    print("Choose CSV file:")
    for key in csv_options:
        print(f"{key}. {csv_options[key]}")

    choice = int(input("Enter choice: "))

    processes = read_csv(csv_options[choice])
    completed, gantt = sjf_scheduling(processes)
    display_results(completed, gantt)
