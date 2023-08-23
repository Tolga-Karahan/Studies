from prefect import context, Flow, Parameter, task
from prefect.tasks.control_flow.filter import FilterTask
from prefect.engine.signals import SKIP

def say_hello():
    print('hello')

@task 
def add_one(x):
    say_hello()
    return x+1

@task
def reduce_task(x):
    return sum(x)

filter_results = FilterTask(
    filter_func=lambda x: not isinstance(x, (BaseException, SKIP, type(None)))
)

@task
def unstable_task(arg):
    if arg == 1:
        raise RuntimeError("Failed")
    if arg == 2:
        raise SKIP("Skipped")
    if arg == 3:
        return None
    
    return arg

@task(log_stdout=True)
def print_result(result):
    print(result)

with Flow("Mapping example flow") as flow:
    # Define a parameter for the input list
    input = Parameter("input")
    # Imperative
    # log_args2 = log_args.copy()
    # add_one.set_upstream(input, key='x', mapped=True)
    # log_args.set_upstream(add_one, key='args')
    # unstable_task.set_upstream(add_one, key='arg')
    # filter_results.set_upstream(unstable_task, key='task_results')
    # log_args2.set_upstream(filter_results, key='args')

    add_one_result = add_one.map(input)
    print_result(add_one_result)
    # unstable_task_result = unstable_task.map(add_one_result)
    # filtered_results = filter_results(unstable_task_result)
    # print_result(filtered_results)
    
state = flow.run(parameters={"input":list(range(10))})
# print(f"Add one results: {state.result[add_one_result]}")
# print(f"Unstable task results: {state.result[unstable_task_result]}")
# print(f"Filtered results: {state.result[filtered_results]}")
