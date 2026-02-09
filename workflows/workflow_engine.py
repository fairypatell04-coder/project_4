def run_workflow(workflow):
    for step in workflow["steps"]:
        print("Running:", step["action"])
