# OPERATING SYSTEMS SIMULATION PROJECT
## CPU scheduling and Deadlock Management using CSV Test Cases
---

## Team Members 

-Prince John Martine 

-Neelam Rajesh

-Ibrahim

## 1. INTRODUCTION
This project is an academic *Operating Systems simulation project* designed to demonstrate and analyze core OS concepts through practical implementation using Python.

The project focuses on:
- CPU Scheduling Algorithms such as First come First served ,Shortet Job First , Round Robin algorithms. 
- Deadlock occurrence and prevention
- Banker’s Algorithm for deadlock avoidance
- Use of CSV files as test cases
- Clear performance analysis and reporting

All simulations are implemented in a structured and modular manner, and all reports are stored *inside the repository*.

---

## 2. PROJECT OBJECTIVES

The objectives of this project are:

- To simulate and understand different CPU scheduling algorithms
- To analyze how arrival time, burst time, and time quantum affect performance
- To observe waiting time and turnaround time variations
- To demonstrate deadlock situations and unsafe states
- To apply Banker’s Algorithm to prevent deadlock
- To organize experiments using multiple CSV test cases
- To produce professional reports with Gantt charts and observations

---

## 3. TECHNOLOGIES USED

- Python 3
- CSV files (for test inputs)
- Git & GitHub (version control)
- Microsoft Word (.docx) for reports

---

## 4. PROJECT DIRECTORY STRUCTURE
OS-Simulation-Project/
│
├── csv_test_files/
│   ├── FCFS_INPUTS/
│   ├── SJF_INPUTS/
│   ├── RR_INPUTS/
│   └── DEADLOCK_TESTS/
│
├── reports/
│   └─── FCFS_REPORT.pdf
     ── sjf reports.pdf
│    ── rr.pdf
│    ── bankers_algorithm.pdf

├── sorce_code/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── rr.py
│   ├── deadlock_detection.py
│   
│
├── README.md
└── .gitignore

---
## 5. CSV FILE FORMAT

### CPU Scheduling CSV Format

```csv
ProcessId,Arrival_Time,Burst_Time
P1,0,5
P2,1,3
P3,2,8

---

##  Deadlock /Bankers Algorithm csv 
PID,Allocation,Max,Available
P1,1 0 1,3 2 2,3 3 2

6. CPU SCHEDULING ALGORITHMS IMPLEMENTED

6.1 First Come First Serve (FCFS)
•	Non-preemptive scheduling algorithm
•	Processes are executed in the order they arrive
•	Simple but may cause the convoy effect

Metrics Calculated:
•	Start Time
•	Completion Time
•	Turnaround Time (TAT)
•	Waiting Time (WT)
•	Average TAT and WT
•	Gantt Chart

⸻

6.2 Shortest Job First (SJF)
•	Non-preemptive scheduling
•	Selects the process with the shortest burst time among arrived processes
•	Minimizes average waiting time
•	May cause starvation of long processes

⸻

6.3 Round Robin (RR)
•	Preemptive scheduling algorithm
•	Each process is given a fixed time quantum
•	Processes are executed in a cyclic order
•	Fair scheduling suitable for time-sharing systems

Key Characteristics:
•	Context switching occurs frequently
•	Waiting time depends on time quantum
•	Prevents starvation

⸻

7. DEADLOCK CONCEPTS

A deadlock occurs when processes are unable to proceed because each is waiting for resources held by others.

Necessary Conditions for Deadlock:
	1.	Mutual Exclusion
	2.	Hold and Wait
	3.	No Preemption
	4.	Circular Wait

The project demonstrates deadlock using unsafe resource allocation states.

⸻

8. BANKER’S ALGORITHM

Banker’s Algorithm is used to avoid deadlock by checking system safety before granting resource requests.

Key Data Structures:
	•	Allocation Matrix
	•	Maximum Matrix
	•	Need Matrix
	•	Available Resources
	•	Safe Sequence

The algorithm ensures the system always remains in a safe state.

⸻

9. USER INTERACTION FLOW
	1.	User runs the main program
	2.	User selects:
	•	Scheduling algorithm (FCFS / SJF / Round Robin / Banker’s)
	•	CSV test case
	3.	Program reads CSV data
	4.	Scheduling or safety analysis is performed
	5.	Results are displayed on the terminal
	6.	Observations are documented in reports

⸻


FCFS REPORT
reports/fcfs_reports/FCFS_REPORT.pdf

The report includes:
	•	All FCFS test cases
	•	Tables of scheduling results
	•	Gantt charts
	•	Observations on:
	•	Process order
	•	Arrival time impact
	•	Waiting time variation

11. SAMPLE GANTT CHART
| P1 | P2 | P3 |
0    5    8   16

12. OBSERVATIONS
	•	FCFS may result in high waiting time
	•	SJF minimizes average waiting time
	•	Round Robin improves fairness
	•	Arrival time significantly affects scheduling order
	•	Unsafe resource allocation leads to deadlock
	•	Banker’s Algorithm successfully prevents deadlock

⸻

13. HOW TO RUN THE PROJECT
 python source_code/foldername.py

 

