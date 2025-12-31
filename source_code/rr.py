import csv
from collections import deque

# ================= Part 1: Process Class =================
class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid                   # Process ID (unique)
        self.arrival = int(arrival)      # Arrival time of process
        self.burst = int(burst)          # CPU burst time
        self.remaining = int(burst)      # Remaining burst time (for RR)
        self.waiting = 0                 # Waiting time (calculated later)
        self.turnaround = 0              # Turnaround time (calculated later)

# ================= Part 2: Round Robin Scheduler Class =================
class RoundRobinScheduler:
    def __init__(self, time_quantum):
        self.time_quantum = time_quantum  # Time quantum for RR
        self.processes = []               # List of processes
        self.gantt_chart = []             # Stores Gantt chart info

    # ===== Part 2a: Load Processes from CSV =====
    def load_processes(self, filename):
        self.processes = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.processes.append(Process(row['ProcessID'], row['ArrivalTime'], row['BurstTime']))
        # Sort by arrival time
        self.processes.sort(key=lambda x: x.arrival)

    # ===== Part 2b: Run the Round Robin Algorithm =====
    def run(self):
        time = 0
        queue = deque()
        processes = self.processes.copy()
        completed = 0
        n = len(processes)

        while completed < n:
            # Add newly arrived processes to the ready queue
            for p in processes:
                if p.arrival <= time and p not in queue and p.remaining > 0:
                    queue.append(p)

            if queue:
                current = queue.popleft()
                exec_time = min(current.remaining, self.time_quantum)
                self.gantt_chart.append((current.pid, time, time + exec_time))
                time += exec_time
                current.remaining -= exec_time

                # Add any processes that arrive during execution
                for p in processes:
                    if p.arrival <= time and p not in queue and p.remaining > 0 and p != current:
                        queue.append(p)

                # If process is not finished, put it back in queue
                if current.remaining > 0:
                    queue.append(current)
                else:
                    # Process finished, calculate waiting & turnaround times
                    current.turnaround = time - current.arrival
                    current.waiting = current.turnaround - current.burst
                    completed += 1
            else:
                # CPU idle
                time += 1

    # ===== Part 2c: Display Results and Gantt Chart =====
    def display_results(self):
        print("\nGantt Chart:")
        for pid, start, end in self.gantt_chart:
            print(f"|{pid}({start}-{end})", end=" ")
        print("|")

        total_waiting = sum(p.waiting for p in self.processes)
        total_turnaround = sum(p.turnaround for p in self.processes)
        n = len(self.processes)

        print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
        for p in self.processes:
            print(f"{p.pid}\t{p.arrival}\t{p.burst}\t{p.waiting}\t{p.turnaround}")

        print(f"\nAverage Waiting Time: {total_waiting/n:.2f}")
        print(f"Average Turnaround Time: {total_turnaround/n:.2f}")

# ================= Part 3: Main Program =================
if __name__ == "__main__":
    # ===== Part 3a: CSV Options =====
    csv_options = {
        1: "csv_test_files/RR_INPUTS/rr_input_case1.csv",
        2: "csv_test_files/RR_INPUTS/rr_inputcase2.csv",
        3: "csv_test_files/RR_INPUTS/rr_input_case3.csv",
        4: "csv_test_files/RR_INPUTS/rr_input_case4.csv"
    }

    print("Select CSV test file:")
    for key, val in csv_options.items():
        print(f"{key}: {val}")

    # ===== Part 3b: User Input =====
    choice = int(input("Enter choice (1-4): "))
    filename = csv_options.get(choice)
    if not filename:
        print("Invalid choice!")
        exit()

    time_quantum = int(input("Enter Time Quantum: "))

    # ===== Part 4: Run Scheduler =====
    rr = RoundRobinScheduler(time_quantum)
    rr.load_processes(filename)
    rr.run()
    rr.display_results()
