# Design-Patterns

# Design Patterns in Python
This repository contains implementations of the **Factory Method** and **Strategy Pattern** in Python.

## Patterns Implemented
- **Factory Method**: Demonstrates creating products through a factory method to abstract the creation process.
- **Strategy Pattern**: Allows dynamic selection of pricing strategies for coffee.

### Factory Method Pattern
- The `Creator` class defines a method `factory_method()` that returns a `Product` object.
- `ConcreteCreatorA` and `ConcreteCreatorB` are subclasses of `Creator` that override `factory_method()` to produce `ConcreteProductA` and `ConcreteProductB`, respectively.

### Strategy Pattern
- The `PricingStrategy` class defines a method `calculate_cost()` that takes a `base_cost`.
- Different strategies like `NoExtraCost`, `MilkPricingStrategy`, and `SugarPricingStrategy` implement `PricingStrategy` to alter the cost of a coffee.
- The `Coffee` class uses a `PricingStrategy` to determine its final cost based on the selected strategy.


## How to Run
- To run the Factory Method example:
  ```bash
  python3 factory_method.py
  ```
- To run the Strategy Pattern example:
  ```bash
  python3 strategy_pattern.py
  ```
##  Factory method Class diagram

https://drive.google.com/file/d/1B6ZIid19UPFZh-vo8lKqAMO4_nrJ7mZA/view?usp=drive_link

##  Strategy method Class diagram

https://drive.google.com/file/d/1alvh3jK65ZwGpfLgsdpYDEf6Ate7SAMJ/view?usp=drive_link