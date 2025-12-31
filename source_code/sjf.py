import csv

# Process class
# Process class represents a single process in CPU scheduling
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid                  # Process ID (unique identifier)
        self.arrival_time = arrival_time  # Time when process enters ready queue
        self.burst_time = burst_time      # CPU time required by the process

        # These will be calculated during scheduling
        self.waiting_time = 0            # Time process waits in ready queue
        self.turnaround_time = 0         # Total time from arrival to completion

# Read CSV file
def read_csv(file_path):
    processes = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append(
                Process(
                    row['pid'],
                    int(row['arrival_time']),
                    int(row['burst_time'])
                )
            )
    return processes


# SJF Scheduling (Non-preemptive)

def sjf_scheduling(processes):
    time = 0
    completed = []
    gantt_chart = []

    processes.sort(key=lambda x: x.arrival)

    while processes:
        available = [p for p in processes if p.arrival <= time]

        if not available:
            time += 1
            continue

        # Select shortest job
        current = min(available, key=lambda x: x.burst)
        processes.remove(current)

        start_time = time
        time += current.burst
        end_time = time

        current.waiting = start_time - current.arrival
        current.turnaround = current.waiting + current.burst

        completed.append(current)
        gantt_chart.append((current.pid, start_time, end_time))

    return completed, gantt_chart


# Display results

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


# Main

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
