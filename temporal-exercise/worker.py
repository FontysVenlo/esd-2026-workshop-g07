import asyncio
import logging
import os

from temporalio.client import Client
from temporalio.worker import Worker

from activities import bake_pizza, charge_card, deliver_pizza
from workflows import PizzaWorkflow

ADDRESS = os.environ.get("TEMPORAL_ADDRESS", "localhost:7233")


async def connect() -> Client:
    # the Temporal server can still be starting up
    for _ in range(30):
        try:
            return await Client.connect(ADDRESS)
        except RuntimeError:
            await asyncio.sleep(1)
    return await Client.connect(ADDRESS)


async def main():
    logging.getLogger("temporalio.activity").setLevel(logging.ERROR)

    client = await connect()
    worker = Worker(
        client,
        task_queue="pizza",
        workflows=[PizzaWorkflow],
        activities=[charge_card, bake_pizza, deliver_pizza],
    )
    print("Worker started, waiting for pizza orders")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
