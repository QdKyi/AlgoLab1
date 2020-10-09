class Bicycle:
    def __init__(self, number_of_gears, weight_in_kg, max_weight, producer_name):
        self.number_of_gears = int(number_of_gears)
        self.weight_in_kg = int(weight_in_kg)
        self.max_weight = max_weight
        self.producer_name = producer_name

    def __repr__(self):
        return f'Number of gears are {self.number_of_gears}, Weight is {self.weight_in_kg}, ' \
            f'Max weight that bicycle can carry is {self.max_weight}, Producer name is {self.producer_name}'