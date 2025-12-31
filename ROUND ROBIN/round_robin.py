"""Self-contained CLI for Round Robin in the ROUND ROBIN folder.

Usage (Windows):
    py -3 round_robin.py --quantum 4 --csv rr_input.csv
"""
import csv
import argparse
from pathlib import Path

from rr import RoundRobinScheduler


def read_processes_from_csv(path):
    p = Path(path)
    if not p.exists():
        return []
    processes = []
    with p.open(newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            try:
                pid = row[0].strip()
                arrival = int(row[1])
                burst = int(row[2])
            except Exception:
                continue
            processes.append((pid, arrival, burst))
    return processes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', default='rr_input.csv')
    parser.add_argument('--quantum', type=int, default=4)
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
