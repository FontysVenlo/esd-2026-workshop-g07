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
        for i in range(count):
            await workflow.execute_activity(
                publish_number,
                FibonacciNumber(i, a),
                start_to_close_timeout=timedelta(seconds=5),
            )
            sequence.append(a)
            a, b = b, a + b
        return sequence
