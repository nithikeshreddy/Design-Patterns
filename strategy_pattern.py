# Strategy Interface
class PricingStrategy:
    def calculate_cost(self, base_cost: int) -> int:
        pass

# Concrete Strategies
class NoExtraCost(PricingStrategy):
    def calculate_cost(self, base_cost: int) -> int:
        return base_cost

class MilkPricingStrategy(PricingStrategy):
    def calculate_cost(self, base_cost: int) -> int:
        return base_cost + 2

class SugarPricingStrategy(PricingStrategy):
    def calculate_cost(self, base_cost: int) -> int:
        return base_cost + 1

# Coffee Class that uses a PricingStrategy
class Coffee:
    def __init__(self, pricing_strategy: PricingStrategy):
        self.pricing_strategy = pricing_strategy
        self.base_cost = 5

    def get_cost(self) -> int:
        return self.pricing_strategy.calculate_cost(self.base_cost)


if __name__ == "__main__":
    plain_coffee = Coffee(NoExtraCost())
    print(f"Plain Coffee Cost: {plain_coffee.get_cost()}")  # Outputs: 5

    milk_coffee = Coffee(MilkPricingStrategy())
    print(f"Milk Coffee Cost: {milk_coffee.get_cost()}")  # Outputs: 7

    sugar_coffee = Coffee(SugarPricingStrategy())
    print(f"Sugar Coffee Cost: {sugar_coffee.get_cost()}")  # Outputs: 6
