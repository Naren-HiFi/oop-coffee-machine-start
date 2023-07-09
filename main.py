from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_menu = Menu()

continue_serving_coffee = False

while not continue_serving_coffee:
    options = coffee_menu.get_items()
    choice = input(f"What would you like: {options}: ")
    if choice == 'off':
        continue_serving_coffee = True
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(choice)
        payment = money_machine.make_payment(drink.cost)
        if coffee_maker.is_resource_sufficient(drink) and payment:
            coffee_maker.make_coffee(drink)
