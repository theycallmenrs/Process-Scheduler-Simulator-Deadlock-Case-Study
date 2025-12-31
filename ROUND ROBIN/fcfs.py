"""
FIRST-COME, FIRST-SERVED (FCFS) CPU SCHEDULING ALGORITHM
"""

class FCFSScheduler:
    def __init__(self):
        self.processes = []
        self.gantt_chart = []
        self.avg_waiting_time = 0
        self.avg_turnaround_time = 0
        self.total_time = 0
    
    def add_process(self, pid, arrival_time, burst_time):
        """Add a process to the scheduler"""
        self.processes.append({
            'pid': pid,
            'arrival_time': arrival_time,
            'burst_time': burst_time,
            'waiting_time': 0,
            'turnaround_time': 0,
            'response_time': 0,
            'completion_time': 0,
            'start_time': 0
        })
    
    def schedule(self):
        """Execute FCFS scheduling"""
        # Sort processes by arrival time
        self.processes.sort(key=lambda x: x['arrival_time'])
        
        current_time = 0
        
        for process in self.processes:
            # Check for idle time
            if process['arrival_time'] > current_time:
                idle_time = process['arrival_time'] - current_time
                self.gantt_chart.append(("IDLE", idle_time))
                current_time = process['arrival_time']
            
            # Execute process
            start_time = current_time
            end_time = current_time + process['burst_time']
            
            self.gantt_chart.append((process['pid'], process['burst_time']))
            
            # Calculate times
            process['completion_time'] = end_time
            process['turnaround_time'] = process['completion_time'] - process['arrival_time']
            process['waiting_time'] = process['turnaround_time'] - process['burst_time']
            process['response_time'] = start_time - process['arrival_time']
            process['start_time'] = start_time
            
            current_time = end_time
        
        self.total_time = current_time
        self._calculate_averages()
    
    def _calculate_averages(self):
        """Calculate average waiting and turnaround times"""
        total_waiting = sum(p['waiting_time'] for p in self.processes)
        total_turnaround = sum(p['turnaround_time'] for p in self.processes)
        self.avg_waiting_time = total_waiting / len(self.processes)
        self.avg_turnaround_time = total_turnaround / len(self.processes)
    
    def display_gantt_chart(self):
        """Display text-based Gantt chart"""
        print("\nGANTT CHART:")
        print("-" * 50)
        
        time = 0
        for pid, duration in self.gantt_chart:
            print(f"[{time:3d} -- {pid:^4} -- {time+duration:3d}]", end=" ")
            time += duration
        print()
    
    def display_results(self):
        """Display complete scheduling results"""
        print("\n" + "="*70)
        print("FIRST-COME, FIRST-SERVED (FCFS) SCHEDULING RESULTS")
        print("="*70)
        
        # Process table
        print("\nPROCESS TABLE:")
        print("-"*70)
        print(f"{'PID':<6} {'Arrival':<8} {'Burst':<6} {'Finish':<7} {'Waiting':<8} {'Turnaround':<10} {'Response':<8}")
        print("-"*70)
        
        for p in self.processes:
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
    
    def display_summary(self):
        """Display summary only"""
        print(f"  Average Waiting Time: {self.avg_waiting_time:.2f}")
        print(f"  Average Turnaround Time: {self.avg_turnaround_time:.2f}")