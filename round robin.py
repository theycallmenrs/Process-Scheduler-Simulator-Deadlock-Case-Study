"""Deprecated compatibility stub.

This file used to contain the Round Robin scheduler implementation.
The canonical implementation now lives in `source_code/rr.py` and
the command-line wrapper is `round_robin.py`.

Keep this small stub to avoid breaking imports that reference the old file name.
"""

from source_code.rr import RoundRobinScheduler
