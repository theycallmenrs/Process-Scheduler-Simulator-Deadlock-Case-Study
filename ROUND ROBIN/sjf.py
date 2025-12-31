"""
SHORTEST JOB FIRST (SJF) CPU SCHEDULING ALGORITHM
Both non-preemptive and preemptive (SRTF) versions
"""

class SJFScheduler:
    def __init__(self, preemptive=False):
        self.preemptive = preemptive
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
            'remaining_time': burst_time,
            'waiting_time': 0,
            'turnaround_time': 0,
            'response_time': -1,
            'completion_time': 0,
            'start_time': -1
        })
    
    def schedule(self):
        """Execute SJF scheduling"""
        if self.preemptive:
            self._schedule_preemptive()
        else:
            self._schedule_non_preemptive()
        
        self._calculate_averages()
    
    def _schedule_non_preemptive(self):
        """Non-preemptive SJF"""
        # Sort by arrival time
        remaining = sorted(self.processes, key=lambda x: x['arrival_time'])
        completed = []
        current_time = 0
        
        while remaining:
            # Get arrived processes
            arrived = [p for p in remaining if p['arrival_time'] <= current_time]
            
            if not arrived:
                # No process arrived, advance time
                next_arrival = min(p['arrival_time'] for p in remaining)
                idle_time = next_arrival - current_time
                if idle_time > 0:
                    self.gantt_chart.append(("IDLE", idle_time))
                current_time = next_arrival
                continue
            
            # Select process with shortest burst time
            current_process = min(arrived, key=lambda x: x['burst_time'])
            remaining.remove(current_process)
            
            # Execute completely
            start_time = current_time
            end_time = current_time + current_process['burst_time']
            
            self.gantt_chart.append((current_process['pid'], current_process['burst_time']))
            
            # Calculate metrics
            current_process['completion_time'] = end_time
            current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
            current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
            current_process['response_time'] = start_time - current_process['arrival_time']
            current_process['start_time'] = start_time
            
            current_time = end_time
            completed.append(current_process)
        
        self.processes = completed
        self.total_time = current_time
    
    def _schedule_preemptive(self):
        """Preemptive SJF (Shortest Remaining Time First - SRTF)"""
        # Sort by arrival time
        processes = sorted(self.processes, key=lambda x: x['arrival_time'])
        current_time = 0
        last_pid = None
        last_start = 0
        
        while any(p['remaining_time'] > 0 for p in processes):
            # Get arrived processes with remaining time
            arrived = [p for p in processes 
                      if p['arrival_time'] <= current_time and p['remaining_time'] > 0]
            
            if not arrived:
                # Idle time
                if last_pid and last_start < current_time:
                    self.gantt_chart.append((last_pid, current_time - last_start))
                    last_pid = None
                
                # Find next arrival
                next_arrivals = [p for p in processes if p['arrival_time'] > current_time]
                if next_arrivals:
                    next_time = min(p['arrival_time'] for p in next_arrivals)
                    idle_time = next_time - current_time
                    if idle_time > 0:
                        self.gantt_chart.append(("IDLE", idle_time))
                    current_time = next_time
                continue
            
            # Select process with shortest remaining time
            current_process = min(arrived, key=lambda x: x['remaining_time'])
            
            # Record response time if first time
            if current_process['response_time'] == -1:
                current_process['response_time'] = current_time - current_process['arrival_time']
                current_process['start_time'] = current_time
            
            # Check if we need to switch processes
            if last_pid != current_process['pid']:
                if last_pid and last_start < current_time:
                    self.gantt_chart.append((last_pid, current_time - last_start))
                
                last_pid = current_process['pid']
                last_start = current_time
            
            # Execute for 1 time unit
            current_process['remaining_time'] -= 1
            current_time += 1
            
            # Check if process completed
            if current_process['remaining_time'] == 0:
                current_process['completion_time'] = current_time
                current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
                current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
        
        # Add last process to Gantt chart
        if last_pid and last_start < current_time:
            self.gantt_chart.append((last_pid, current_time - last_start))
        
        self.total_time = current_time
    
    def _calculate_averages(self):
        """Calculate average waiting and turnaround times"""
        total_waiting = sum(p['waiting_time'] for p in self.processes)
        total_turnaround = sum(p['turnaround_time'] for p in self.processes)
        self.avg_waiting_time = total_waiting / len(self.processes)
        self.avg_turnaround_time = total_turnaround / len(self.processes)
    
    def display_results(self):
        """Display complete scheduling results"""
        algo_type = "PREEMPTIVE SJF (SRTF)" if self.preemptive else "NON-PREEMPTIVE SJF"
        
        print("\n" + "="*70)
        print(f"{algo_type} SCHEDULING RESULTS")
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
        print("\nGANTT CHART:")
        print("-" * 50)
        
        time = 0
        for pid, duration in self.gantt_chart:
            print(f"[{time:3d} -- {pid:^4} -- {time+duration:3d}]", end=" ")
            time += duration
        print()
        
        # Statistics
        print("\n" + "-"*40)
        print("PERFORMANCE METRICS")
        print("-"*40)
        print(f"Average Waiting Time:    {self.avg_waiting_time:.2f}")
        print(f"Average Turnaround Time: {self.avg_turnaround_time:.2f}")
        print(f"Throughput: {len(self.processes)/self.total_time:.3f} processes/unit time")
        print(f"Algorithm Type: {'Preemptive' if self.preemptive else 'Non-preemptive'}")
    
    def display_summary(self):
        """Display summary only"""
        algo_type = "SJF-P" if self.preemptive else "SJF-NP"
        print(f"{algo_type}:")
        print(f"  Average Waiting Time: {self.avg_waiting_time:.2f}")
        print(f"  Average Turnaround Time: {self.avg_turnaround_time:.2f}")