import asyncio
from dataclasses import dataclass

from temporalio import activity
from temporalio.exceptions import ApplicationError


@dataclass
class PizzaOrder:
    order_id: str
    pizza: str
    card: str


@activity.defn
async def charge_card(order: PizzaOrder) -> str:
    if order.card == "declined":
        print(f"[charge_card] Card declined for {order.order_id} (attempt {activity.info().attempt})")
        raise ApplicationError("The bank declined the card", type="CardDeclined")
    await asyncio.sleep(1)
    print(f"[charge_card] Charged the card for {order.order_id}")
    return f"payment-{order.order_id}"


@activity.defn
async def bake_pizza(order: PizzaOrder) -> None:
    attempt = activity.info().attempt
    await asyncio.sleep(1)
    if attempt < 3:
        print(f"[bake_pizza] The oven is still cold (attempt {attempt})")
        raise ApplicationError("The oven is still cold")
    print(f"[bake_pizza] Baked a {order.pizza} pizza (attempt {attempt})")


@activity.defn
async def deliver_pizza(order: PizzaOrder) -> None:
    attempt = activity.info().attempt
    print(f"[deliver_pizza] Delivering {order.order_id}... (attempt {attempt})")
    await asyncio.sleep(8)
    print(f"[deliver_pizza] Delivered {order.order_id}")
