class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered:
            return self.pizza_already_ordered()
        if ingredient not in self.ingredients:
            self.ingredients.setdefault(ingredient, 0)
        self.ingredients[ingredient] += quantity
        self.price += price_per_ingredient * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered:
            return self.pizza_already_ordered()
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= price_per_ingredient * quantity

    def pizza_already_ordered(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        # if self.ordered:
        #     return self.pizza_already_ordered()
        order = ""
        self.ordered = True
        order += f"You've ordered pizza {self.name} prepared with "
        order += ", ".join([f"{name}: {quantity}" for name, quantity in self.ingredients.items()])
        order += f" and the price will be {self.price}lv."
        return order


margarita = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
print(margarita.make_order())
print(margarita)
print(margarita.add_extra('mozzarella', 1, 2))
print(margarita.remove_ingredient('mozzarella', 1, 2))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)

# print(margarita.add_extra('cheese', 1, 1))
