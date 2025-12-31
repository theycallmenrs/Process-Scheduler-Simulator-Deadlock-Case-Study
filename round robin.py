"""Deprecated compatibility stub.

This file used to contain the Round Robin scheduler implementation.
The canonical implementation now lives in `source_code/rr.py` and
the command-line wrapper is `round_robin.py`.

Keep this stub to avoid breaking imports that reference the old file name.
"""

from source_code.rr import RoundRobinScheduler  # re-export for compatibility
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
        """Execute Round Robin scheduling algorithm"""
        # Sort processes by arrival time
        sorted_processes = sorted(self.processes, key=lambda x: x['arrival_time'])
        
        # Initialize ready queue and remaining processes
        ready_queue = deque()
        remaining_processes = sorted_processes.copy()
        current_time = 0
        last_pid = None
        last_start = 0
        
        # Add initial arrivals
        for p in remaining_processes[:]:
            if p['arrival_time'] <= current_time:
                ready_queue.append(p)
                remaining_processes.remove(p)
        
        while ready_queue or remaining_processes:
            if not ready_queue:
                # No processes ready, advance time to next arrival
                next_arrival = min(p['arrival_time'] for p in remaining_processes)
                idle_time = next_arrival - current_time
                if idle_time > 0:
                    self.gantt_chart.append(("IDLE", idle_time))
                    last_pid = None
                current_time = next_arrival
                
                # Add newly arrived processes
                for p in remaining_processes[:]:
                    if p['arrival_time'] <= current_time:
                        ready_queue.append(p)
                        remaining_processes.remove(p)
                continue
            
            # Get next process from ready queue
            current_process = ready_queue.popleft()
            
            # Record response time if first time
            if current_process['response_time'] == -1:
                current_process['response_time'] = current_time - current_process['arrival_time']
                current_process['start_time'] = current_time
            
            # Determine execution time (minimum of time quantum or remaining time)
            execution_time = min(self.time_quantum, current_process['remaining_time'])
            
            # Update Gantt chart
            if last_pid != current_process['pid']:
                if last_pid and last_start < current_time:
                    self.gantt_chart.append((last_pid, current_time - last_start))
                last_pid = current_process['pid']
                last_start = current_time
            
            # Execute the process
            current_process['remaining_time'] -= execution_time
            current_time += execution_time
            
            # Add newly arrived processes during execution
            for p in remaining_processes[:]:
                if p['arrival_time'] <= current_time:
                    ready_queue.append(p)
                    remaining_processes.remove(p)
            
            # Check if process completed
            if current_process['remaining_time'] == 0:
                current_process['completion_time'] = current_time
                current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
                current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
            else:
                # Process not finished, add back to ready queue
                ready_queue.append(current_process)
        
        # Add last process to Gantt chart
        if last_pid and last_start < current_time:
            self.gantt_chart.append((last_pid, current_time - last_start))
        
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
        print("-" * 70)
        
        time = 0
        line1 = ""
        line2 = ""
        
        for pid, duration in self.gantt_chart:
            # Top line with times
            line1 += f" {time:3d} "
            if duration > 1:
                line1 += " " * (duration * 4 - 4)
            
            # Process execution line
            line2 += "|"
            if pid == "IDLE":
                line2 += "----" * duration
            else:
                line2 += f"{pid:^3}" + "---" * (duration - 1)
            
            time += duration
        
        line1 += f" {time:3d}"
        line2 += "|"
        
        print(line1)
        print(line2)
        
        # Timeline
        print("\nTimeline:")
        time = 0
        for pid, duration in self.gantt_chart:
            print(f"[{time:3d}-{pid}-{time+duration:3d}]", end=" ")
            time += duration
        print()
    
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
        print(f"  Average Turnaround Time: {self.avg_turnaround_time:.2f}")