from math import hypot

from ..sample import Sample
from distance import Distance


class EuclideanDistance(Distance):
    def calculate_distance(self, s1: Sample, s2: Sample) -> float:
        return hypot(
            s1.petal_length - s2.petal_length,
            s1.petal_width - s2.petal_width,
            s1.sepal_length - s2.sepal_length,
            s1.sepal_width - s2.sepal_width,
        )
