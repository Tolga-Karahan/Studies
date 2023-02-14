from ..sample import Sample
from distance import Distance


class ChebyshevDistance(Distance):
    def calculate_distance(self, s1: Sample, s2: Sample) -> float:
        return max(
            abs(s1.petal_length - s2.petal_length),
            abs(s1.petal_width - s2.petal_width),
            abs(s1.sepal_length - s2.sepal_length),
            abs(s1.sepal_width - s2.sepal_width),
        )
