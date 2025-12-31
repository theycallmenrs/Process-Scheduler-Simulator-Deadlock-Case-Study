#!/usr/bin/env python3
"""
MAIN PROGRAM: CPU Scheduler Simulator & Deadlock Detection
Complete solution with all required algorithms
"""

import os
import sys
import csv
from datetime import datetime

class Process:
    """Process class for all schedulers"""
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.completion_time = 0
        self.start_time = 0

def clear_screen():
    """Clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print program header"""
    print("\n" + "="*80)
    print(" "*25 + "CPU SCHEDULER SIMULATOR")
    print(" "*28 + "& DEADLOCK DETECTION")
    print("="*80)

# Import scheduler modules
sys.path.append(os.path.dirname(__file__))

try:
    from scheduler_fcfs import FCFSScheduler
    from scheduler_sjf import SJFScheduler
    from scheduler_round_robin import RoundRobinScheduler
    from banker_algorithm import BankersAlgorithm
    print("✓ All modules loaded successfully!")
except ImportError as e:
    print(f"✗ Error loading modules: {e}")
    print("Please ensure all scheduler files are in the same directory.")
    sys.exit(1)

def load_processes_from_csv(filename):
    """Load processes from CSV file"""
    processes = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pid = row.get('Process', row.get('PID', 'P1'))
                arrival = int(row.get('Arrival_Time', 0))
                burst = int(row.get('Burst_Time', 1))
                processes.append(Process(pid, arrival, burst))
        
        print(f"✓ Loaded {len(processes)} processes from {filename}")
        return processes
    
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' not found!")
        return None
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        return None

def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("MAIN MENU")
    print("="*60)
    print("1. First-Come, First-Served (FCFS) Scheduling")
    print("2. Shortest Job First (SJF) Scheduling")
    print("3. Round Robin (RR) Scheduling")
    print("4. Deadlock Detection (Banker's Algorithm)")
    print("5. Run All Algorithms (Comparative Analysis)")
    print("6. Generate Test Cases")
    print("7. View Documentation")
    print("8. Exit Program")
    print("="*60)
    return input("Enter your choice (1-8): ")

def run_fcfs():
    """Run FCFS scheduling"""
    print("\n" + "="*60)
    print("FIRST-COME, FIRST-SERVED (FCFS) SCHEDULING")
    print("="*60)
    
    processes = load_processes_from_csv("test_cases/processes_fcfs.csv")
    if not processes:
        processes = [
            Process("P1", 0, 8),
            Process("P2", 1, 4),
            Process("P3", 2, 9),
            Process("P4", 3, 5)
        ]
    
    scheduler = FCFSScheduler()
    for p in processes:
        scheduler.add_process(p.pid, p.arrival_time, p.burst_time)
    
    scheduler.schedule()
    scheduler.display_results()

def run_sjf():
    """Run SJF scheduling"""
    print("\n" + "="*60)
    print("SHORTEST JOB FIRST (SJF) SCHEDULING")
    print("="*60)
    
    print("\nSJF Variants:")
    print("1. Non-preemptive SJF")
    print("2. Preemptive SJF (Shortest Remaining Time First)")
    choice = input("Choose variant (1-2): ")
    preemptive = (choice == '2')
    
    processes = load_processes_from_csv("test_cases/processes_sjf.csv")
    if not processes:
        processes = [
            Process("P1", 0, 7),
            Process("P2", 2, 4),
            Process("P3", 4, 1),
            Process("P4", 5, 4)
        ]
    
    scheduler = SJFScheduler(preemptive=preemptive)
    for p in processes:
        scheduler.add_process(p.pid, p.arrival_time, p.burst_time)
    
    scheduler.schedule()
    scheduler.display_results()

def run_round_robin():
    """Run Round Robin scheduling"""
    print("\n" + "="*60)
    print("ROUND ROBIN (RR) SCHEDULING")
    print("="*60)
    
    time_quantum = int(input("Enter time quantum (default=4): ") or "4")
    
    processes = load_processes_from_csv("test_cases/processes_rr.csv")
    if not processes:
        processes = [
            Process("P1", 0, 10),
            Process("P2", 1, 5),
            Process("P3", 2, 8),
            Process("P4", 3, 2)
        ]
    
    scheduler = RoundRobinScheduler(time_quantum=time_quantum)
    for p in processes:
        scheduler.add_process(p.pid, p.arrival_time, p.burst_time)
    
    scheduler.schedule()
    scheduler.display_results()

def run_deadlock_detection():
    """Run Banker's Algorithm"""
    print("\n" + "="*60)
    print("DEADLOCK DETECTION - BANKER'S ALGORITHM")
    print("="*60)
    
    banker = BankersAlgorithm()
    
    while True:
        print("\nOptions:")
        print("1. Display system state")
        print("2. Check safe state")
        print("3. Simulate resource request")
        print("4. Run example scenario")
        print("5. Return to main menu")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == '1':
            banker.display_state()
        elif choice == '2':
            is_safe, sequence = banker.is_safe_state()
            if is_safe:
                print(f"\n✓ System is SAFE! Sequence: {' → '.join(sequence)}")
            else:
                print("\n✗ System is UNSAFE! Deadlock possible.")
        elif choice == '3':
            try:
                pid = int(input("Process ID (0-4): "))
                print("Enter request (e.g., '1 0 2'): ")
                request = list(map(int, input().split()))
                banker.request_resources(pid, request)
            except:
                print("Invalid input!")
        elif choice == '4':
            banker.run_example()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to continue...")

def run_all_algorithms():
    """Run all algorithms for comparison"""
    print("\n" + "="*80)
    print("COMPARATIVE ANALYSIS OF ALL SCHEDULING ALGORITHMS")
    print("="*80)
    
    # Common test case
    processes = [
        Process("P1", 0, 8),
        Process("P2", 1, 4),
        Process("P3", 2, 9),
        Process("P4", 3, 5),
        Process("P5", 4, 2)
    ]
    
    print("\nTest Case:")
    for p in processes:
        print(f"  {p.pid}: Arrival={p.arrival_time}, Burst={p.burst_time}")
    
    results = []
    
    # FCFS
    print("\n" + "-"*60)
    print("1. FCFS:")
    fcfs = FCFSScheduler()
    for p in processes:
        fcfs.add_process(p.pid, p.arrival_time, p.burst_time)
    fcfs.schedule()
    fcfs.display_summary()
    results.append(("FCFS", fcfs.avg_waiting_time, fcfs.avg_turnaround_time))
    
    # SJF Non-preemptive
    print("\n" + "-"*60)
    print("2. SJF (Non-preemptive):")
    sjf_np = SJFScheduler(preemptive=False)
    for p in processes:
        sjf_np.add_process(p.pid, p.arrival_time, p.burst_time)
    sjf_np.schedule()
    sjf_np.display_summary()
    results.append(("SJF-NP", sjf_np.avg_waiting_time, sjf_np.avg_turnaround_time))
    
    # SJF Preemptive
    print("\n" + "-"*60)
    print("3. SJF (Preemptive - SRTF):")
    sjf_p = SJFScheduler(preemptive=True)
    for p in processes:
        sjf_p.add_process(p.pid, p.arrival_time, p.burst_time)
    sjf_p.schedule()
    sjf_p.display_summary()
    results.append(("SJF-P", sjf_p.avg_waiting_time, sjf_p.avg_turnaround_time))
    
    # Round Robin Q=4
    print("\n" + "-"*60)
    print("4. Round Robin (Q=4):")
    rr4 = RoundRobinScheduler(time_quantum=4)
    for p in processes:
        rr4.add_process(p.pid, p.arrival_time, p.burst_time)
    rr4.schedule()
    rr4.display_summary()
    results.append(("RR-Q4", rr4.avg_waiting_time, rr4.avg_turnaround_time))
    
    # Round Robin Q=2
    print("\n" + "-"*60)
    print("5. Round Robin (Q=2):")
    rr2 = RoundRobinScheduler(time_quantum=2)
    for p in processes:
        rr2.add_process(p.pid, p.arrival_time, p.burst_time)
    rr2.schedule()
    rr2.display_summary()
    results.append(("RR-Q2", rr2.avg_waiting_time, rr2.avg_turnaround_time))
    
    # Comparison table
    print("\n" + "="*80)
    print("COMPARISON SUMMARY")
    print("="*80)
    print(f"\n{'Algorithm':<15} {'Avg Waiting':<15} {'Avg Turnaround':<15} Best For")
    print("-"*80)
    
    best_wait = min(results, key=lambda x: x[1])[0]
    best_turn = min(results, key=lambda x: x[2])[0]
    
    for name, wait, turn in results:
        best_for = []
        if name == best_wait:
            best_for.append("Waiting")
        if name == best_turn:
            best_for.append("Turnaround")
        best_str = ", ".join(best_for) if best_for else "-"
        
        print(f"{name:<15} {wait:<15.2f} {turn:<15.2f} {best_str}")
    
    print("-"*80)

def generate_test_cases():
    """Generate test CSV files"""
    os.makedirs("test_cases", exist_ok=True)
    
    # FCFS test case
    with open("test_cases/processes_fcfs.csv", 'w') as f:
        f.write("Process,Arrival_Time,Burst_Time\n")
        f.write("P1,0,8\nP2,1,4\nP3,2,9\nP4,3,5\n")
    
    # SJF test case
    with open("test_cases/processes_sjf.csv", 'w') as f:
        f.write("Process,Arrival_Time,Burst_Time\n")
        f.write("P1,0,7\nP2,2,4\nP3,4,1\nP4,5,4\n")
    
    # RR test case
    with open("test_cases/processes_rr.csv", 'w') as f:
        f.write("Process,Arrival_Time,Burst_Time\n")
        f.write("P1,0,10\nP2,1,5\nP3,2,8\nP4,3,2\n")
    
    print("✓ Test cases generated in 'test_cases/' folder")

def main():
    """Main program loop"""
    clear_screen()
    print_header()
    
    # Create directories
    os.makedirs("test_cases", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    
    print("\nInitializing CPU Scheduler Simulator...")
    
    # Generate test cases if needed
    if not os.path.exists("test_cases/processes_fcfs.csv"):
        generate_test_cases()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            clear_screen()
            print_header()
            run_fcfs()
        
        elif choice == '2':
            clear_screen()
            print_header()
            run_sjf()
        
        elif choice == '3':
            clear_screen()
            print_header()
            run_round_robin()
        
        elif choice == '4':
            clear_screen()
            print_header()
            run_deadlock_detection()
        
        elif choice == '5':
            clear_screen()
            print_header()
            run_all_algorithms()
        
        elif choice == '6':
            generate_test_cases()
        
        elif choice == '7':
            print("\nDocumentation:")
            print("1. README.md - Project overview")
            print("2. docs/ - Detailed documentation")
            print("3. Deadlock_Case_Study.pdf - Real-world case study")
        
        elif choice == '8':
            print("\nThank you for using CPU Scheduler Simulator!")
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice! Please enter 1-8.")
        
        input("\nPress Enter to continue...")
        clear_screen()
        print_header()

if __name__ == "__main__":
    main()