import queue
import threading
import time

"""
Prompt:

A compiler thread continuously produces compiled artifacts and puts them on a queue.
A pool of N validator threads consume from the queue and validate each artifact.
The compiler will eventually signal it is done.
Implement the full pipeline so that all artifacts get validated and all threads shut down cleanly when work is complete.

Constraints:

1 producer, 3 consumer threads
Producer generates 15 artifacts then stops
No threads should hang after all work is done
Print each result as it completes


"""
import queue


def compile_artifact(artifact_id):
    """Simulates compilation time"""
    time.sleep(0.1)
    return f"artifact_{artifact_id}"


def validate_artifact(artifact):
    """Simulates validation on hardware"""
    time.sleep(0.3)
    return f"{artifact}_validated"


# Your implementation here
def run_pipeline(num_artifacts, num_validators):
    q = queue.Queue(maxsize=num_artifacts)

    def producer():
        for i in range(num_artifacts):
            artifact = compile_artifact(i)
            q.put(artifact)

        for i in range(num_validators):
            q.put(None)
        return

    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    def consumer():

        while True:
            artifact = q.get()
            if artifact is None:
                break
            validated_artifact = validate_artifact(artifact)
            print(validated_artifact)

    consumer_threads = []
    for _ in range(num_validators):
        thread = threading.Thread(target=consumer)
        consumer_threads.append(thread)

    for t in consumer_threads:
        t.start()

    producer_thread.join()

    for t in consumer_threads:
        t.join()


run_pipeline(num_artifacts=15, num_validators=3)
