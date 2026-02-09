# core/workflow.py
import logging

class WorkflowEngine:
    """
    Simple workflow engine to run tasks in order.
    Tasks should be callable functions.
    """

    def __init__(self, name="Default Workflow"):
        self.name = name
        self.tasks = []

    def add_task(self, task, *args, **kwargs):
        """
        Add a task (function) to the workflow.
        `task` must be callable.
        """
        if not callable(task):
            raise ValueError("Task must be a callable function")
        self.tasks.append((task, args, kwargs))
        logging.info(f"Task '{task.__name__}' added to workflow '{self.name}'")

    def run(self):
        """
        Run all tasks in order.
        """
        logging.info(f"Starting workflow '{self.name}' with {len(self.tasks)} tasks")
        for task, args, kwargs in self.tasks:
            try:
                logging.info(f"Running task: {task.__name__}")
                task(*args, **kwargs)
            except Exception as e:
                logging.error(f"Task '{task.__name__}' failed: {e}")
        logging.info(f"Workflow '{self.name}' completed")
