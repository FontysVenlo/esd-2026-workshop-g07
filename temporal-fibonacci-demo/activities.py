import asyncio
from dataclasses import dataclass

from temporalio import activity


@dataclass
class FibonacciNumber:
    index: int
    value: int


@activity.defn
async def publish_number(number: FibonacciNumber) -> None:
    # pretend this is a slow call to an external service
    await asyncio.sleep(1)

    attempt = activity.info().attempt
    retry = f" (attempt {attempt})" if attempt > 1 else ""
    print(f"F({number.index}) = {number.value}{retry}")
