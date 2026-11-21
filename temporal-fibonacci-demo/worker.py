import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import publish_number
from workflows import FibonacciWorkflow


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="fibonacci",
        workflows=[FibonacciWorkflow],
        activities=[publish_number],
    )
    print("Worker started, press Ctrl+C to stop it")
    await worker.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Worker stopped")
