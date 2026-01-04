import csv
from collections import deque

#  Part 1: Process Class 

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
        """Display complete scheduling results"""
        print("\n" + "="*70)
        print(f"ROUND ROBIN SCHEDULING RESULTS (Time Quantum = {self.time_quantum})")
        print("="*70)
        
        # Process table
        print("\nPROCESS TABLE:")
        print("-"*70)
        print(f"{'PID':<6} {'Arrival':<8} {'Burst':<6} {'Finish':<7} {'Waiting':<8} {'Turnaround':<10} {'Response':<8}")
        print("-"*70)
        
        for p in sorted(self.processes, key=lambda x: x['pid']):
            print(f"{p['pid']:<6} {p['arrival_time']:<8} {p['burst_time']:<6} "
                  f"{p['completion_time']:<7} {p['waiting_time']:<8} "
                  f"{p['turnaround_time']:<10} {p['response_time']:<8}")
        
        # Gantt chart
        self.display_gantt_chart()
        
        # Statistics
        print("\n" + "-"*40)
        print("PERFORMANCE METRICS")
        print("-"*40)
        print(f"Average Waiting Time:    {self.avg_waiting_time:.2f}")
        print(f"Average Turnaround Time: {self.avg_turnaround_time:.2f}")
        print(f"Throughput: {len(self.processes)/self.total_time:.3f} processes/unit time")
        print(f"Total Execution Time: {self.total_time}")
    
    def display_summary(self):
        """Display summary only"""
        print(f"  Average Waiting Time: {self.avg_waiting_time:.2f}")
        print(f"  Average Turnaround Time: {self.avg_turnaround_time:.2f}")  these are the codes  and do you mean like this