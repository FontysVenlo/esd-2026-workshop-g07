import asyncio
import os
import random
import sys

from temporalio.client import Client
from temporalio.common import WorkflowIDConflictPolicy

from activities import PizzaOrder
from workflows import PizzaWorkflow

ADDRESS = os.environ.get("TEMPORAL_ADDRESS", "localhost:7233")


async def main():
    declined = len(sys.argv) > 1 and sys.argv[1] == "declined"
    order = PizzaOrder(
        order_id="pizza-declined" if declined else f"pizza-{random.randint(1000, 9999)}",
        pizza="margherita",
        card="declined" if declined else "4242",
    )

    client = await Client.connect(ADDRESS)
    handle = await client.start_workflow(
        PizzaWorkflow.run,
        order,
        id=order.order_id,
        task_queue="pizza",
        id_conflict_policy=WorkflowIDConflictPolicy.TERMINATE_EXISTING,
    )
    print(f"Order placed: {order.order_id}")
    print(f"Web UI: http://localhost:8233/namespaces/default/workflows/{order.order_id}")
    print("Waiting for the result... (Ctrl+C stops waiting, the order keeps going)")

    result = await handle.result()
    print("Result:", result)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped waiting. The order is still in Temporal.")
        os._exit(0)
