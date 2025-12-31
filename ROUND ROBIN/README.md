ROUND ROBIN
============

This folder contains helper files for the Round Robin scheduler.

Files:
- `run_round_robin.bat` — Windows helper to run the top-level `round_robin.py` CLI.
- `RR_REPORT.txt` — placeholder for generated reports.

How to run (Windows PowerShell/CMD):

Open a terminal in this repository root and run:

    py -3 round_robin.py --quantum 4

Or from this folder (Windows):

    ROUND ROBIN\run_round_robin.bat

Notes:
- The canonical scheduler implementation lives in `source_code/rr.py`.
- The CLI wrapper is `round_robin.py` at the repository root.
