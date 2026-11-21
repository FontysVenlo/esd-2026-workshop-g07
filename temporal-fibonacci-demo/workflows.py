from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import FibonacciNumber, publish_number


@workflow.defn
class FibonacciWorkflow:
    @workflow.run
    async def run(self, count: int) -> list[int]:
        sequence: list[int] = []
        a, b = 0, 1
        replayed = 0
        for i in range(count):
            # only for the demo: show which numbers came from the Event History
            if replayed and not workflow.unsafe.is_replaying():
                print(f"Replay: F(0) to F({replayed - 1}) came from the Event History, not published again")
                replayed = 0

            await workflow.execute_activity(
                publish_number,
                FibonacciNumber(i, a),
                start_to_close_timeout=timedelta(seconds=5),
            )
            if workflow.unsafe.is_replaying():
                replayed = i + 1

            sequence.append(a)
            a, b = b, a + b
        return sequence
