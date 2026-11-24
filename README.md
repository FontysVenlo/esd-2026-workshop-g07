# Temporal - workflow orchestration technology - ESD 2026

## Fibonacci Demo

Needs Python 3.11+ and the Temporal CLI.

```bash
# setup (once)
cd temporal-fibonacci-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# terminal 1: Temporal server, Web UI at http://localhost:8233
temporal server start-dev

# terminal 2: worker (Ctrl+C to stop it, run again to restart)
python worker.py

# terminal 3: start the workflow
python starter.py
```

Terminals 2 and 3 run inside `temporal-fibonacci-demo` with `source .venv/bin/activate`.

## Workshop exercise - The Pizza Shop

You get a small pizza shop. A pizza order has three steps: **charge the card**, **bake the pizza** and **deliver it**. The steps are already written. You write the part that says in which order they run, and then you try to break the shop: an oven that fails, a worker that crashes and a card that is declined. Temporal keeps the order going.

Words you will meet:

- **Activity:** one step that does real work, like `charge_card`. They are in `activities.py` and are already done.
- **Workflow:** the recipe: which step runs when. It's in `workflows.py`. **This is the only file you change.**
- **Worker:** the program that runs your workflow and activities. It runs in a Docker container.
- **Temporal Service:** remembers every finished step in the **Event History**. It runs in another Docker container and has a Web UI at http://localhost:8233.
- **Docker container:** a ready-made mini computer on your laptop. You don't install anything yourself.

## Before you start

1. Start **Docker Desktop**.
2. Clone this repository and open a terminal in the `temporal-exercise` folder:

```bash
git clone https://github.com/FontysVenlo/esd-2026-workshop-g07.git
cd esd-2026-workshop-g07/temporal-exercise
```

3. Build and start everything:

```bash
docker compose up -d --build
```

4. Open http://localhost:8233 in your browser. This is the Temporal Web UI. The list is still empty.

5. Open **two terminals**, both in the `temporal-exercise` folder:
   - **Terminal 1, the kitchen:** shows what the worker is doing. Run this and keep it open:

     ```bash
     docker compose logs -f worker
     ```

   - **Terminal 2, the customer:** you type all the other commands here.

6. Open `workflows.py` in any editor. If your editor says it can't find `temporalio`, ignore it: the code runs inside Docker, not on your laptop.

## Step 1: Write the workflow

Open `workflows.py`. Replace the line `# TODO step 1: paste the code from the README here` with this code (keep the indentation):

```python
        await workflow.execute_activity(
            charge_card,
            order,
            start_to_close_timeout=timedelta(seconds=10),
        )
        await workflow.execute_activity(
            bake_pizza,
            order,
            start_to_close_timeout=timedelta(seconds=10),
        )
        await workflow.execute_activity(
            deliver_pizza,
            order,
            start_to_close_timeout=timedelta(seconds=15),
        )
```

Save the file. The worker only reads your code when it starts, so restart it. In **terminal 2**:

```bash
docker compose restart worker
```

Now place an order, also in **terminal 2**:

```bash
docker compose run --rm order
```

Watch **terminal 1**. You should see something like this:

```
[charge_card] Charged the card for pizza-1432
[bake_pizza] The oven is still cold (attempt 1)
[bake_pizza] The oven is still cold (attempt 2)
[bake_pizza] Baked a margherita pizza (attempt 3)
[deliver_pizza] Delivering pizza-1432... (attempt 1)
[deliver_pizza] Delivered pizza-1432
```

After about 15 seconds, terminal 2 prints `Result: pizza-1432: delivered` (your order number is different).

Now open the link that terminal 2 printed (or click your order in the Web UI) and look at the **Event History**: every step of your order, with its result.

**Note:**
- How many times did `bake_pizza` run? Who made it try again? Did you write a retry loop?

## Step 2: Pull the plug 

Now you crash the worker in the middle of an order.

1. In **terminal 2**, place a new order:

   ```bash
   docker compose run --rm order
   ```

2. Wait until **terminal 1** shows `Delivering pizza-...`. Then, quickly, in **terminal 2**:
   - press `Ctrl+C` (you stop waiting for the result, the order keeps going), then
   - crash and restart the worker:

     ```bash
     docker compose restart worker
     ```

Keep watching **terminal 1**. You will see `Worker started` and, after about 15 seconds, `Delivering pizza-... (attempt 2)` and then `Delivered`. Open the order in the Web UI: its status is **Completed**.

**Note:**
- Look at the log in terminal 1. For this order, how many times was the card charged? How many times was the pizza baked?
- Why didn't the new worker start again from the beginning? (Hint: Event History.)
- Why did it take a few seconds before the delivery was tried again? (Hint: `start_to_close_timeout`.)

## Step 3: A declined card

1. In **terminal 2**, place an order with a card that is always declined:

   ```bash
   docker compose run --rm order declined
   ```

2. Watch **terminal 1**: `Card declined (attempt 1)`, `(attempt 2)`, `(attempt 3)`... with longer and longer waits in between. By default, Temporal retries a failed activity **forever**. That's great for a short network problem, but a declined card will never work.
3. Press `Ctrl+C` in **terminal 2**. The order is still retrying inside Temporal: you can see it in the Web UI.

Now fix it. In `workflows.py`, replace the **first** `execute_activity` (the one for `charge_card`) with this code:

```python
        try:
            await workflow.execute_activity(
                charge_card,
                order,
                start_to_close_timeout=timedelta(seconds=10),
                retry_policy=RetryPolicy(non_retryable_error_types=["CardDeclined"]),
            )
        except ActivityError:
            return f"{order.order_id}: cancelled, the card was declined"
```

Save, restart the worker and try again, in **terminal 2**:

```bash
docker compose restart worker
docker compose run --rm order declined
```

Terminal 2 now prints `Result: pizza-declined: cancelled, the card was declined`. (Placing the order again automatically replaces the old one that was still retrying.)

**Note:**
- What is one error that *should* be retried, and one that should *not*.

## Done early?

- Stop the worker with `docker compose stop worker` and place an order in terminal 2. Nothing happens. Wait 20 seconds, then start the worker in terminal 1 with `docker compose start worker` and `docker compose logs -f worker`. What happens to the order that was waiting?
- In the Web UI, open `pizza-declined` and find the error message of the failed activity.


## Sources

All sources are listed in [`temporal-sources.md`](temporal-sources.md).
