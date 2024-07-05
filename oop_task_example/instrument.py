from math import sqrt
class Triangle:
    def __init__(self, side_A_pm, side_B_pm, siad_C_pm, ):
        self.said_a = side_A_pm
        self.said_b = side_B_pm
        self.said_c = siad_C_pm

    def perimeter(self):
        result = self.said_a + self.said_b + self.said_c
        return result
    def calculate_s(self):
        p = (self.said_a + self.said_b + self.said_c)/2
        geron = p * (p - self.said_a) * (p - self.said_b) * (p - self.said_c)
        sqrt_resalut = sqrt(geron)
        return sqrt_resalut



triangle = Triangle(side_A_pm=10, side_B_pm=10, siad_C_pm=10, )

print(triangle.calculate_s())

print(triangle.perimeter())
