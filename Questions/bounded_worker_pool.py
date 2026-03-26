"""
Prompt:

You have a fleet of N hardware boards and M jobs to validate. Each job must run on exactly one board.
Only N jobs can run simultaneously (one per board).
Implement a system that processes all jobs concurrently, respects the board limit,
and returns a dictionary of results when all jobs are complete.

Constraints:

N = 3 boards, M = 10 jobs
run_on_board(job_id, board_id) is provided — treat it as a black box that takes ~0.5s
Return {job_id: "passed"} for each job
"""

import queue
import threading
from concurrent.futures import ThreadPoolExecutor


def run_on_board(job_id, board_id):
    pass


def run():
    M = 10
    N = 3

    q = queue.Queue()

    for i in range(M):
        q.put(i)

    def board_task(board_id):

        while not q.empty():
            try:
                job_id = q.get(block=False)  # raises queue.Empty if nothing left
            except queue.Empty:
                break
            run_on_board(job_id, board_id)
            q.task_done()

    threads = []
    for i in range(N):
        thread = threading.Thread(target=board_task, args=(i,))
        threads.append(thread)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
