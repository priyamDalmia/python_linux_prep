import os 

# # 15. 
# 1. Ability to make three hot flavours 
from common import COFFEE_RECIPES

class CoffeeMachine:
    COFFEE_RECIPES = COFFEE_RECIPES
    def __init__(self, water=0, milk=0, coffee=0) -> None:
        self.water = water 
        self.milk = milk
        self.coffee = coffee
        self.money = 0 
        pass

    def insert_money(self):
        print(f"Please insert coins.")
        quarters = input(f"How many quarters?: ")
        dimes = input(f"How many dimes?: ")
        nickles = input(f"How many nickles?: ")
        pennies = input(f"How many pennies?: ")
        self.money += (
            (int(quarters) * 0.25)
            + (int(dimes) * 0.1)
            + (int(nickles) * 0.20)
            + (int(pennies) * 0.01)
        ) 
        return 
    
    def report(self) -> None:
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: {self.money}")
        return 
    
    def make_coffee(self, resources_required) -> None:
        self.water -= resources_required['water']
        self.milk -= resources_required['milk']
        self.coffee -= resources_required['coffee']
        print(f"Here's your {resources_required['coffee_type']}!")
        return 
    
    def check_resources_sufficient(self, coffee_type):
        confirm = False 
        resources_required = dict()
        resources_for_coffee = self.COFFEE_RECIPES[coffee_type]['ingredients']
        resources_required['coffee_type'] = coffee_type
        resources_required['cost'] = self.COFFEE_RECIPES[coffee_type]['cost']

        for resource in ['water', 'milk', 'coffee']:
            attr = getattr(self, resource)
            resources_required[resource] = resources_for_coffee[resource]
            if resources_for_coffee[resource] > attr:
                confirm = False
                resources_required[resource] = attr
                return confirm, resources_required
            else:
                confirm = True 
        return confirm, resources_required


    def start(self):
        user_choice = input("What would you like? (espresso/latte/cappuccino): ") 

        if user_choice == 'report':
            self.report()
        elif user_choice in self.COFFEE_RECIPES.keys():
            confirm_order, resources_required = self.check_resources_sufficient(user_choice)
            if confirm_order:
                self.insert_money()
                if self.money >= resources_required['cost']:
                    self.make_coffee(resources_required)
                    print(f"Here's your change: {self.money}")
                    self.money = 0
                else:
                    print("Insufficient Money!")
                    self.money = 0
                    return
            else:
                print(f"Not enough {list(resources_required.keys())[-1]}.") 
        else:
            raise Exception("Invalid Option! Try again.")
        return 

if __name__ == "__main__":
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    coffee_machine = CoffeeMachine(**resources)

    while True:
        try:
            coffee_machine.start()
        except Exception as e:
            print(e.message)
            break 