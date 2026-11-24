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
        try:
            await workflow.execute_activity(
                charge_card,
                order,
                start_to_close_timeout=timedelta(seconds=10),
                retry_policy=RetryPolicy(non_retryable_error_types=["CardDeclined"]),
            )
        except ActivityError:
            return f"{order.order_id}: cancelled, the card was declined"
        await workflow.execute_activity(
            bake_pizza,
            order,
            start_to_close_timeout=timedelta(seconds=10),
        )
        await workflow.execute_activity(
            deliver_pizza,
            order,
            start_to_close_timeout=timedelta(seconds=20),
        )

        return f"{order.order_id}: delivered"
