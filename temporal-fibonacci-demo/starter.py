import asyncio

from temporalio.client import Client

from workflows import FibonacciWorkflow


async def main():
    client = await Client.connect("localhost:7233")
    handle = await client.start_workflow(
        FibonacciWorkflow.run,
        30,
        id="fibonacci-demo",
        task_queue="fibonacci",
    )
    print("Started workflow fibonacci-demo")
    print("Web UI: http://localhost:8233/namespaces/default/workflows/fibonacci-demo")

    result = await handle.result()
    print("Result:", result)


if __name__ == "__main__":
    asyncio.run(main())
