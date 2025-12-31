"""Command-line wrapper for the Round Robin scheduler.

Usage:
  py -3 round_robin.py [--csv path/to/file.csv] [--quantum N]

If no CSV is provided or the CSV is empty, a built-in demo process list is used.
CSV format (no header required): pid,arrival_time,burst_time
"""
import csv
import sys
import argparse
from pathlib import Path

from source_code.rr import RoundRobinScheduler


def read_processes_from_csv(path):
    path = Path(path)
    if not path.exists():
        return []
    processes = []
    try:
        with path.open(newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                # allow rows like: pid, arrival, burst
                try:
                    pid = row[0].strip()
                    arrival = int(row[1])
                    burst = int(row[2])
                except Exception:
                    continue
                processes.append((pid, arrival, burst))
    except Exception:
        return []
    return processes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', help='Path to CSV input', default='csv_test_files/RR_INPUTS/rr_input 1.csv')
    parser.add_argument('--quantum', help='Time quantum (integer)', type=int, default=4)
    args = parser.parse_args()

    processes = read_processes_from_csv(args.csv)

    if not processes:
        processes = [
            ('P1', 0, 5),
            ('P2', 1, 3),
            ('P3', 2, 8),
            ('P4', 3, 6),
        ]
        print('No CSV input found or file empty — using built-in demo processes.')

    scheduler = RoundRobinScheduler(time_quantum=args.quantum)
    for pid, arrival, burst in processes:
        scheduler.add_process(pid, arrival, burst)

    scheduler.schedule()
    scheduler.display_results()


if __name__ == '__main__':
    main()
