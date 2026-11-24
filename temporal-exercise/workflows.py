from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.exceptions import ActivityError

with workflow.unsafe.imports_passed_through():
    from activities import PizzaOrder, bake_pizza, charge_card, deliver_pizza


@workflow.defn
class PizzaWorkflow:
    @workflow.run
    async def run(self, order: PizzaOrder) -> str:
#Paste


        return f"{order.order_id}: delivered"
