from prefect import Flow, Parameter, task, Task

# Each step is a task. A task can be created by just 
# decorating a function.
@task
def say_hello(persons: str):
    for person in persons:
        print(f"Hello, {person}!")


# Tasks can optionally accept inputs and produce outputs.
@task
def add(param1: int, param2: int = 7):
    return param1 + param2


# Tasks can be defined via classes as well. Especially if
# the underlying task is complex. To do it Task class is
# inherited, __init__ and run methods are implemented.
class Add(Task):
    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, param1: int, param2: int = None) -> int:
        if param2 is None:
            param2 = self.default
        return param1 + param2


add_task = Add(default=7)

# Prefect's functional API can be used to create flows.
# Calls are made as if they are simple functions. Prefect
# takes care of tracking them and building a graph that
# is representing the flow.
with Flow("My first flow") as flow:
    first_result = add(3, 5)
    second_result = add(first_result, 7)

    # Run the flow
    # If flow has a schedule, call will sleep until next
    # scheduled time. Then it will run and sleep for next
    # time again and so on...
    state = flow.run()

    # Get states of each individual task
    first_task_state = state.result[first_result]
    second_task_state = state.result[second_result]

    assert state.is_successful()
    assert first_task_state.is_successful()
    assert second_task_state.is_successful()


# Flows can be parameterized as well
with Flow("Parameterized Flow") as flow:
    name = Parameter("name")
    say_hello(name)

    # Run the flow with a parameter
    flow.run(name="Tolga")

# Prefect's imperative API can be used to build workflow
# in more explicit way
flow = Flow("My first imperative flow")

name = Parameter("name")
second_add = add.copy()

flow.add_task(add)
flow.add_task(second_add)
flow.add_task(say_hello)

# Make second_add upsteam of say_hello task so that it
# waits upstream task to finish. It is called a state
# dependency or non-data dependency
say_hello.set_upstream(second_add, flow=flow)

# Create data bindings
# Functional and Imperative APIs can be mixed for
# example to use context manager instead of passing
# flows manually
add.bind(param1=3, param2=5, flow=flow)
second_add.bind(param1=add, param2=7, flow=flow)
say_hello.bind(person=name, flow=flow)
