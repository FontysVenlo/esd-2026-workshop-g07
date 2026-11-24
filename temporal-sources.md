# Sources

All sources used for the Temporal workshop: the slides, the script, the demo and the exercise.
Slide numbers refer to `TemporalWorkshop .pptx` (42 slides). All links were checked on 22 November 2026.

## What Temporal is

1. Temporal Technologies. (n.d.). *What is Temporal?* Temporal documentation. https://docs.temporal.io/temporal
   Used for: durable execution and what Temporal is (slides 7 to 10).
2. Temporal Technologies. (n.d.). *About Temporal.* https://temporal.io/about
   Used for: where Temporal comes from. The founders built Cadence at Uber, worked on AWS Simple Workflow Service and created the Azure Durable Task Framework (slide 9).
3. Cadence project. (n.d.). *Cadence Workflow: Open source durable execution engine.* https://cadenceworkflow.io/
   Used for: Cadence, the workflow engine the Temporal founders built at Uber before Temporal (slide 9).
4. Temporal Technologies. (n.d.). *temporalio/temporal* [Source code]. GitHub. https://github.com/temporalio/temporal
   Used for: the Temporal Service is open source under the MIT licence (slide 9).
5. Temporal Technologies. (n.d.). *Develop durable applications with Temporal SDKs.* Temporal documentation. https://docs.temporal.io/develop
   Used for: the list of SDK languages (slide 9).
6. Temporal Technologies. (n.d.). *Temporal Cloud guide.* Temporal documentation. https://docs.temporal.io/cloud
   Used for: self-hosting versus the managed Temporal Cloud (slides 9 and 13).
7. Temporal Technologies. (n.d.). *Durable Execution Solutions* [Homepage]. https://temporal.io/
   Used for: use cases and the companies that use Temporal (slide 11).
8. Temporal Technologies. (n.d.). *Customer stories.* https://temporal.io/in-use
   Used for: use cases and the companies that use Temporal (slide 11).

## Building blocks: workflows, activities, workers and clients

9. Temporal Technologies. (n.d.). *Temporal Workflow.* Temporal documentation. https://docs.temporal.io/workflows
   Used for: what a workflow is and the workflow-or-activity quiz (slides 13, 14 and 16 to 22).
10. Temporal Technologies. (n.d.). *What is a Temporal Activity?* Temporal documentation. https://docs.temporal.io/activities
    Used for: what an activity is and the quiz (slides 15 to 22).
11. Temporal Technologies. (n.d.). *What is a Temporal Worker?* Temporal documentation. https://docs.temporal.io/workers
    Used for: workers and the big picture (slides 13 and 23).
12. Temporal Technologies. (n.d.). *Task Queues.* Temporal documentation. https://docs.temporal.io/task-queue
    Used for: workers poll task queues; tasks wait when no worker is running (slide 23).
13. Temporal Technologies. (n.d.). *Workflow Id and Run Id.* Temporal documentation. https://docs.temporal.io/workflow-execution/workflowid-runid
    Used for: only one running workflow can have a given Workflow ID (slide 24).

## Surviving crashes

14. Temporal Technologies. (n.d.). *Events and Event History.* Temporal documentation. https://docs.temporal.io/workflow-execution/event
    Used for: the Event History and replay (slides 26 and 27).
15. Temporal Technologies. (n.d.). *Temporal Workflow Definition.* Temporal documentation. https://docs.temporal.io/workflow-definition
    Used for: workflow code must be deterministic (slides 14 and 29).
16. Temporal Technologies. (n.d.). *Temporal Python SDK sandbox environment.* Temporal documentation. https://docs.temporal.io/develop/python/python-sdk-sandbox
    Used for: the Python sandbox that catches non-deterministic code (slide 29).

## Handling failure

17. Temporal Technologies. (n.d.). *Detecting Activity failures.* Temporal documentation. https://docs.temporal.io/encyclopedia/detecting-activity-failures
    Used for: the four activity timeouts and heartbeats (slide 31).
18. Temporal Technologies. (n.d.). *What is a Temporal Retry Policy?* Temporal documentation. https://docs.temporal.io/encyclopedia/retry-policies
    Used for: the default retry policy values and non-retryable errors (slide 32).
19. Temporal Technologies. (n.d.). *Activity Definition.* Temporal documentation. https://docs.temporal.io/activity-definition
    Used for: activities should be idempotent (slide 33).

## Beyond the basics

20. Temporal Technologies. (n.d.). *Temporal Workflow message passing: Signals, Queries, & Updates.* Temporal documentation. https://docs.temporal.io/encyclopedia/workflow-message-passing
    Used for: signals, queries and updates, and that queries also work on completed workflows (slide 35).
21. Temporal Technologies. (n.d.). *Timers and Start Delays.* Temporal documentation. https://docs.temporal.io/workflow-execution/timers-delays
    Used for: durable timers (slide 36).
22. Fortuna, E. (2023, May 24). *Saga design pattern explained: Benefits, use cases, and implementation.* Temporal blog. https://temporal.io/blog/saga-pattern-made-easy
    Used for: the saga pattern with compensations (slide 37).
23. Garcia-Molina, H., & Salem, K. (1987). Sagas. *Proceedings of the 1987 ACM SIGMOD International Conference on Management of Data*, 249–259. https://doi.org/10.1145/38713.38742
    Used for: where the saga pattern comes from (slide 37).
24. Temporal Technologies. (n.d.). *Versioning* (Python SDK). Temporal documentation. https://docs.temporal.io/develop/python/versioning
    Used for: patching running workflows (slide 38).
25. Temporal Technologies. (n.d.). *Worker Versioning.* Temporal documentation. https://docs.temporal.io/worker-versioning
    Used for: Worker Versioning (slide 38).

## Alternatives

26. Amazon Web Services. (n.d.). *What is Step Functions?* AWS documentation. https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
    Used for: AWS Step Functions in the comparison (slide 40).
27. Amazon Web Services. (n.d.). *Using Amazon States Language to define Step Functions workflows.* AWS documentation. https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html
    Used for: Step Functions workflows are JSON state machines (slide 40).
28. Microsoft. (n.d.). *Durable Functions overview.* Microsoft Learn. https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview
    Used for: Azure Durable Functions in the comparison (slide 40).
29. Microsoft. (n.d.). *Durable orchestrator code constraints.* Microsoft Learn. https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-code-constraints
    Used for: Durable Functions also replays code and needs deterministic orchestrators (slide 40).
30. The Apache Software Foundation. (n.d.). *What is Airflow?* Apache Airflow documentation. https://airflow.apache.org/docs/apache-airflow/stable/index.html
    Used for: Airflow workflows are Python DAGs for batch workflows (slide 40).
31. Camunda. (n.d.). *Modeling with BPMN.* Camunda 8 documentation. https://docs.camunda.io/docs/components/modeler/bpmn/
    Used for: Camunda processes are modelled in BPMN (slide 40).

## Code, tools and further learning

32. Temporal Technologies. (n.d.). *Python SDK developer guide.* Temporal documentation. https://docs.temporal.io/develop/python
    Used for: the Python code on the slides (slides 14, 15, 23, 24, 32, 33, 36 and 37), the Fibonacci demo and the exercise.
33. Temporal Technologies. (n.d.). *temporalio/sdk-python* [Source code]. GitHub. https://github.com/temporalio/sdk-python
    Used for: the Python SDK used in the demo and the exercise.
34. Temporal Technologies. (n.d.). *temporalio* (Version 1.36.1) [Python package]. PyPI. https://pypi.org/project/temporalio/
    Used for: the SDK version pinned in `temporal-fibonacci-demo/requirements.txt`.
35. Temporal Technologies. (n.d.). *Temporal CLI server command reference.* Temporal documentation. https://docs.temporal.io/cli/server
    Used for: `temporal server start-dev` and the Web UI on port 8233 (slide 42 and the demo).
36. Temporal Technologies. (n.d.). *Temporal Web UI.* Temporal documentation. https://docs.temporal.io/web-ui
    Used for: reading the Event History in the Web UI (slides 26 and 28, the demo).
37. Temporal Technologies. (n.d.). *temporalio/temporal* [Docker image]. Docker Hub. https://hub.docker.com/r/temporalio/temporal
    Used for: running the Temporal dev server in Docker for the exercise.
38. Temporal Technologies. (n.d.). *Learn Temporal.* https://learn.temporal.io/
    Used for: further learning and free courses (slide 42).
