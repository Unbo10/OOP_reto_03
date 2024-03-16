from datetime import date
from datetime import datetime

class MenuItem:
    def __init__(self) -> None:
        self._name: str = ""
        self._price: float = 0
        self._change_log: list = []
        self._discount: float = 0

class FoodItem(MenuItem):
    def __init__(self) -> None:
        super().__init__()
        self._is_fried: bool = False
        self._is_spicy: bool = False
        self._is_vegan: bool = False
        self._is_vegetarian: bool = False
        self._is_gluten_free: bool = False
        self._is_chef_suggestion: bool = False
        self._is_nut_free: bool = False
        self._secret_ingredients: list = []
        self._shareable_ingredients: list = []

    def calculate_discount(self, order) -> None:
        summary = order.get_summary()
        j = -1
        for i in summary:
            if i._name == self._name:
                j += 1
                self._discount = self._price * (j * 0.025)
    
    def set_name(self, name: str, waiter) -> None:
        self._name = name
        self._change_log.append(f"Name changed to {name} by {waiter.name}")

    def get_name(self) -> str:
        return self._name

    def set_is_fried(self, is_fried: bool) -> None:
        self._is_fried = is_fried

    def get_is_fried(self) -> bool:
        return self._is_fried

    def set_is_spicy(self, is_spicy: bool) -> None:
        self._is_spicy = is_spicy

    def get_is_spicy(self) -> bool:
        return self._is_spicy

    def set_is_vegan(self, is_vegan: bool) -> None:
        self._is_vegan = is_vegan

    def get_is_vegan(self) -> bool:
        return self._is_vegan

    def set_is_vegetarian(self, is_vegetarian: bool) -> None:
        self._is_vegetarian = is_vegetarian

    def get_is_vegetarian(self) -> bool:
        return self._is_vegetarian

    def set_is_gluten_free(self, is_gluten_free: bool) -> None:
        self._is_gluten_free = is_gluten_free

    def get_is_gluten_free(self) -> bool:
        return self._is_gluten_free

    def set_is_chef_suggestion(self, is_chef_suggestion: bool) -> None:
        self._is_chef_suggestion = is_chef_suggestion

    def get_is_chef_suggestion(self) -> bool:
        return self._is_chef_suggestion

    def set_is_nut_free(self, is_nut_free: bool) -> None:
        self._is_nut_free = is_nut_free

    def get_is_nut_free(self) -> bool:
        return self._is_nut_free
    
    def set_price(self, price: float, waiter) -> None:
        self._price = price
        self._change_log.append(f"Price changed to {price} by {waiter.name}")

    def get_price(self) -> float:
        return self._price
    
    def get_change_log(self) -> list:
        return self._change_log
    
    def get_secret_ingredients(self, password: str) -> list:
        if password == "OOP":
            return self._secret_ingredients
        else:
            print("Invalid password")

    def set_secret_ingredients(self, ingredients: list, password: str, waiter):
        if password == "OOP":
            self._secret_ingredients = ingredients
            self._change_log.append(f"Secret ingredients changed to {ingredients} by {waiter.name}")
        else:
            print("Invalid password")

    def get_shareable_ingredients(self):
        return self._shareable_ingredients

    def set_shareable_ingredients(self, ingredients: list, password: str, waiter):
        if password == "OOP":
            self._shareable_ingredients = ingredients
            self._change_log.append(f"Shareable ingredients changed to {ingredients} by {waiter.name}")
        else:
            print("Invalid password")

class Appetizer(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Empanadas"
        self._price = 5
        self.set_shareable_ingredients(ingredients=["Dough", "Meat", "Onion", "Garlic", "Cumin", "Paprika", "Salt", "Pepper"], password="OOP", waiter=waiter)
        self._is_vegan = False
        self._is_vegetarian = False
        self._is_gluten_free = False
        self._is_nut_free = True
        self._is_chef_suggestion = True
    

class Soup(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Tomato soup"
        self._price = 7
        self.set_shareable_ingredients(ingredients=["Tomato", "Onion", "Garlic", "Basil", "Olive oil", "Salt", "Pepper"], password="OOP", waiter=waiter)
        self._is_vegan = True
        self._is_vegetarian = True
        self._is_gluten_free = True
        self._is_nut_free = True
        self._is_chef_suggestion = False

class MainCourse(FoodItem):
    def __init__(self) -> None:
        super().__init__()

class Pasta(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Pasta"
        self._price = 10
        self.set_shareable_ingredients(ingredients=["Pasta", "Bolognesa sauce", "Cheese"], password="OOP", waiter=waiter)
        self._is_vegan = False
        self._is_vegetarian = False
        self._is_gluten_free = False
        self._is_nut_free = True
        self._is_chef_suggestion = False

class Hamburger(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Hamburger"
        self._price = 8
        self.set_shareable_ingredients(ingredients=["Bread", "Meat", "Lettuce", "Tomato", "Onion", "Cheese", "Ketchup", "Mustard"], password="OOP", waiter=waiter)
        self._is_vegan = False
        self._is_vegetarian = False
        self._is_gluten_free = False
        self._is_nut_free = True
        self._is_chef_suggestion = False
    
class Pizza(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Pizza"
        self._price = 9
        self.set_shareable_ingredients(ingredients=["Dough", "Tomato sauce", "Cheese", "Pepperoni", "Mushrooms", "Onion", "Pepper", "Olive oil"], password="OOP", waiter=waiter)
        self._is_vegan = False
        self._is_vegetarian = False
        self._is_gluten_free = False
        self._is_nut_free = True
        self._is_chef_suggestion = False

class HotDog(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Hot dog"
        self._price = 6
        self.set_shareable_ingredients(ingredients=["Bread", "Sausage", "Ketchup", "Mustard", "Onion"], password="OOP", waiter=waiter)
        self._is_vegan = False
        self._is_vegetarian = False
        self._is_gluten_free = False
        self._is_nut_free = True
        self._is_chef_suggestion = False

class Salad(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Ceaser Salad"
        self._price = 7
        self._is_vegan = False
        self._is_vegetarian = True
        self._is_gluten_free = True
        self._is_nut_free = True
        self._is_chef_suggestion = True
        self.set_shareable_ingredients(ingredients=["Lettuce", "Croutons", "Parmesan cheese", "Caesar dressing"], password="OOP", waiter=waiter)

class Traditional(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Bandeja Paisa"
        self._price = 12
        self._is_vegan = False
        self._is_vegetarian = False
        self._is_gluten_free = False
        self._is_nut_free = True
        self._is_chef_suggestion = True
        self.set_shareable_ingredients(ingredients=["Rice", "Beans", "Egg", "Pork belly", "Sausage", "Arepa", "Avocado", "Plantain", "Salad"], password="OOP", waiter=waiter)

    def calculate_discount(self, order) -> None:
        super().calculate_discount(order)
        self._discount += self._price*(0.05)

class Dessert(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Arroz con leche"
        self._price = 4
        self._is_vegan = False
        self._is_vegetarian = True
        self._is_gluten_free = False
        self._is_nut_free = True
        self._is_chef_suggestion = True
        self.set_shareable_ingredients(ingredients=["Rice", "Milk", "Sugar", "Cinnamon"], password="OOP", waiter=waiter)
        self.set_secret_ingredients(ingredients=["Vanilla", "Condensed milk"], password="OOP", waiter=waiter)


class DrinkItem(MenuItem):
    def __init__(self):
        super().__init__()
        self._is_alcoholic: bool = False
        self._is_carbonated: bool = False
        self._ice: bool = False
        self._refill: bool = False
        self._age_restriction: bool = False
        self._expiration_date: date = date.today()
        self._brand: str = ""
        self._flavor: str = ""
        self._volume: float = 0.0
   
    def is_alcoholic(self):
        return self._is_alcoholic

    def is_alcoholic(self, value):
        self._is_alcoholic = value
    
    def is_carbonated(self):
        return self._is_carbonated

    def is_carbonated(self, value):
        self._is_carbonated = value

    def ice(self):
        return self._ice

    def ice(self, value):
        self._ice = value
    
    def refill(self):
        return self._refill

    def refill(self, value):
        self._refill = value
    
    def age_restriction(self):
        return self._age_restriction

    def age_restriction(self, value):
        self._age_restriction = value
    
    def expiration_date(self):
        return self._expiration_date

    def expiration_date(self, value):
        self._expiration_date = value
    
    def brand(self):
        return self._brand

    def brand(self, value):
        self._brand = value
    
    def flavor(self):
        return self._flavor

    def flavor(self, value):
        self._flavor = value
    
    def volume(self):
        return self._volume

    def volume(self, value):
        self._volume = value

class NonAlcoholic(DrinkItem):
    def __init__(self):
        super().__init__()
        self._is_alcoholic = False
        self._is_homemade = True

class Water(NonAlcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Water"
        self._price = 1
        self._is_carbonated = False
        self._brand = "Tata's"
        self._flavor = "Natural"
        self._volume = 0.5
        self._is_tap = True

class Juice(NonAlcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Juice"
        self._price = 2
        self._is_carbonated = False
        self._brand = "Tata's"
        self._flavor = "Orange"
        self._volume = 0.5
        self._is_homemade = True

class TemperanceDrink(NonAlcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Temperance drink"
        self._price = 5
        self._is_carbonated = True
        self._brand = "Athletic"
        self._flavor = "Beer"
        self._volume = 0.5
        self._is_homemade = False

class Alcoholic(DrinkItem):
    def __init__(self):
        super().__init__()
        self._is_alcoholic = True
        self._is_homemade = False

class Beer(Alcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Beer"
        self._price = 4
        self._is_carbonated = True
        self._brand = "Club Colombia"
        self._flavor = "Beer"
        self._type = "Gold"
        self._volume = 3
        self._is_homemade = False

class Wine(Alcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Wine"
        self._price = 10
        self._is_carbonated = False
        self._brand = "Santa Helena"
        self._flavor = "Sweet"
        self._type = "Cabernet Sauvignon"
        self._volume = 12
        self._is_homemade = False

class Cocktail(Alcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Cocktail"
        self._price = 8
        self._is_carbonated = False
        self._brand = "Tata's"
        self._flavor = "Margarita"
        self._volume = 8
        self._is_homemade = True
    

class Order:
    def __init__(self, items: list) -> None:
        self.__status: str = ""
        self.__customer: Customer = None
        self.__summary: list = []
        self.__tip: float = 0

    def print_summary(self) -> list:
        print(self.__summary)
        for i in self.__summary:
            i.calculate_discount(self)
            print(i._name, end="")
            print(" $", end="")
            print(round(i._price - i._discount, 4), end="")
            if i._discount > 0:
                print("(-", end="")
                print(round((i._discount/i._price)*100, 3), end="")
                print("%)", end=")")
            print()
        print("Tip:", order.__tip, end="")
        print("%")

    def get_summary(self) -> list:
        return self.__summary

    def calculate_total(self) -> float:
        total: float = 0
        for item in self.__summary:
            item.calculate_discount(self)
            total += round((item._price - item._discount), 4)
        total += round(total * (self.__tip / 100), 4)
        total = round(total, 2)
        return total
    
    def set_status(self, status: str) -> None:
        self.status = status

    def get_satus (self, status: str) -> str:
        return self.status
    
    def add_item(self, item) -> None:
        self.__summary.append(item)

    def add_summary(self, item) -> None:
        self.__summary.append(item)

    def set_tip(self, tip: float) -> None:
        self.__tip = tip

    def get_tip(self) -> float:
        return self.__tip

    def set_costumer(self, customer, waiter):
        self.__customer = customer
        waiter.add_remove_customer(customer, "add")

    def get_costumer(self):
        return self.__customer
    
class Waiter:
    def __init__(self, wname: str) -> None:
        self.name: str = wname
        self.__tips: float = 0
        self.__id: str = 0
        self.__customers: list = []

    def add_remove_customer(self, customer, action: str) -> None:
        if action == "add":
            self.__customers.append(customer)
        elif action == "remove":
            self.__customers.remove(customer)
        else:
            print("Invalid action")

    def greet(self) -> None:
        print("Welcome to Tata's! My name is {}, I'll be your waiter today. 😊".format(self.name))
        print("May you give me your name please? ")

    def take_order(self, order: Order, customer) -> None:
        order.status = "open"
        order.customer = customer

    def bring_order(self, customer) -> None:
        print("Here is your order")
        print("Enjoy your meal! 😊")
        # time = datetime.now()
        # while (datetime.now() - time).seconds < 5:
        #     pass

    def calculate_tip(self, order: Order, giv_tip: float) -> None:
        order.set_tip(giv_tip)
        self.__tips += order.calculate_total() * (giv_tip / 100)


class Customer:
    def __init__(self, name: str, balance: float = 100) -> None:
        self.name: float = name

    def order(self, items: list, waiter: Waiter) -> None:
        order: Order = Order(items)
        waiter.take_order(order, self)
    
    def ask_for_bill(self, order: Order, waiter: Waiter, tip: float) -> None:
        order.status = "closed"
        waiter.calculate_tip(order, tip)

    def pay(self, order: Order) -> None:
        amount = order.calculate_total()
        print("Here is your oder summary: ")
        order.print_summary()
        print("Your total is: {}".format(amount))
        print("How would you like to pay? (card/cash)")
        payment = input()
        if payment == "card":
            print("Please enter your card number")
            card = input()
        if payment == "cash":
            pass
        print("Thank you for coming to Tata's! Your payment was succesful")
        print("Have a nice day! 😊")

if __name__ == "__main__":
    waiter: Waiter = Waiter("John")
    waiter.greet()
    customer_name = str(input(""))
    customer: Customer = Customer(customer_name)
    print("A pleasure to meet you {}".format(customer.name))
    print("What would you like to order today?")

    order: Order = Order([])
    order.set_status("open")
    order.set_costumer(customer, waiter)

    print("Here is the menu:")
    print("For appetizers we got: ")
    print("1. Empanadas - $5")
    print("2. Tomato soup - $7")

    print("Now for the main course we have: ")
    print("3. Pasta - $10")
    print("Junk food: ")
    print("4. Hamburger - $8")
    print("5. Pizza - $9")
    print("6. Hot dog - $6")
    print("Salad if you're going fit: ")
    print("7. Caesar salad - $7")
    print("And if you want to go Colombian : ")
    print("8. Bandeja paisa - $12")

    print("Finally, for deserte we have our top-tier: ")
    print("9. Arroz con leche - $4")

    print("To drink we also have a variety of options: ")
    print("Non-alcoholic: ")
    print("10. Water - $1")
    print("11. Juice - $2")
    print("13. Temperance drink - $5")
    print("Alcoholic: ")
    print("14. Beer - $4")
    print("15. Wine - $10")
    print("16. Cocktail - $8")

    done_ordering: bool = False
    items: list = []
    i = -1
    print("What would you like to order? (Please enter the number of the item you want to order. To finish your order type non-numerical characters): ")
    while (not done_ordering):
        item = input("")
        if (item.isdigit()):
            if item == "1":
                items.append(Appetizer())
                order.add_summary(items[i])
                i += 1
            elif item == "2":
                items.append(Soup())
                order.add_summary(items[i])
                i += 1
            elif item == "3":
                items.append(Pasta())
                order.add_summary(items[i])
                i += 1
            elif item == "4":
                items.append(Hamburger())
                order.add_summary(items[i])
                i += 1
            elif item == "5":
                items.append(Pizza())
                order.add_summary(items[i])
                i += 1
            elif item == "6":
                items.append(HotDog())
                order.add_summary(items[i])
                i += 1
            elif item == "7":
                items.append(Salad())
                order.add_summary(items[i])
                i += 1
            elif item == "8":
                items.append(Traditional())
                order.add_summary(items[i])
                i += 1
            elif item == "9":
                items.append(Dessert())
                order.add_summary(items[i])
                i += 1
            elif item == "10":
                items.append(Water())
                order.add_summary(items[i])
                i += 1
            elif item == "11":
                items.append(Juice())
                order.add_summary(items[i])
                i += 1
            elif item == "12":
                items.append(TemperanceDrink())
                order.add_summary(items[i])
                i += 1
            elif item == "13":
                items.append(Beer())
                order.add_summary(items[i])
                i += 1
            elif item == "14":
                items.append(Wine())
                order.add_summary(items[i])
                i += 1
            elif item == "15":
                items.append(Cocktail())
                order.add_summary(items[i])
                i += 1
            else:
                print("Invalid item")
        else:
            done_ordering = True

    print("Alright! I'll bring your order right away")
    # time = datetime.now()
    # while (datetime.now() - time).seconds < 5:
    #     pass
    waiter.bring_order(customer)
    bill = ""
    i = 1
    while bill != "yes":
        print("Will you like your bill? (yes/no)")
        bill = input()
        if bill != "yes":
            print("Alright! I'll be back in a few minutes")
            # time = datetime.now()
            # while (datetime.now() - time).seconds < i * 5:
            #     pass
            i += 1
    print("How much would you like to tip? (Please enter the percentage of the total)")
    tip = float(input())
    customer.ask_for_bill(order, waiter, tip)
    waiter.calculate_tip(order, tip)
    customer.pay(order=order)



    

