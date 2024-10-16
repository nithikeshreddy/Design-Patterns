from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Products
class ConcreteProductA(Product):
    def display(self):
        print("Concrete Product A")

class ConcreteProductB(Product):
    def display(self):
        print("Concrete Product B")

# Creator class
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self):
        # Uses the product created by the factory method
        product = self.factory_method()
        product.display()

# Concrete Creators
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    creator_a.some_operation()  # Outputs: "Concrete Product A"

    creator_b = ConcreteCreatorB()
    creator_b.some_operation()  # Outputs: "Concrete Product B"
