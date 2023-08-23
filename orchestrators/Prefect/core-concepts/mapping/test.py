from random import sample

from prefect import Flow, Parameter, Task, unmapped

class GetNumbers(Task):
    def run(self, total):
        return sample(range(100), total)

class OutputValue(Task):
    def run(self, n, multiple):
        print(n * multiple)

with Flow("unmapped-values") as flow:

    # total = Parameter("total")
    # multiple = Parameter("multiple")

    numbers = GetNumbers()

    output_value = OutputValue()
    output_value.set_upstream(numbers, key="n", mapped=True, flow=flow)

    total = numbers.bind(total=10)
    output_value.bind(n=total, multiple=5)