from datetime import datetime

class MenuItem:
    def __init__(self) -> None:
        self._name: str = ""
        self._price: float = 0
        self._code: int = 0
        self._description: str = ""
        self._discount: float = 0
        self._discount_price: float = 0
        self._is_traditional: bool = False
        self._is_seasonal: bool = False

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_description(self) -> str:
        return self._description
    
    def get_code(self) -> int:
        return self._code
    
    def get_discount(self) -> float:
        return self._discount

    def get_is_traditional(self) -> bool:
        return self._is_traditional
    
    def get_is_seasonal(self) -> bool:
        return self._is_seasonal
    
    def get_price_after_discount(self) -> float:
        return self._price - self._discount_price

    def set_discount(self, discount: float) -> None:
        self._discount = round(discount * 100, 2)
        self._discount_price = round(discount * self._price, 2)

class FoodItem(MenuItem):
    def __init__(self) -> None:
        super().__init__()

class Appetizer(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._price = 5

class Empanada(Appetizer):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Empanada"
        self._description = "A fried dough filled with meat, rice and potatoes you cannot miss"
        self._code = 1
        self._is_traditional = True

class CheeseStick(Appetizer):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Cheese sticks"
        self._description = "The good ol' cheese sticks"
        self._code = 2

class MainCourse(FoodItem):
    def __init__(self) -> None:
        super().__init__()

class Pasta(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Pasta"
        self._price = 10
        self._description = "The go-to when you're feeling Italian, mixed with the best bolonese sauce"
        self._code = 3

class Hamburger(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Hamburger"
        self._price = 8
        self._description = "You'll be surprised by the amount of flavor in this burger with bacon, cheese, lettuce, tomato and our special sauce"
        self._code = 4
    
class Pizza(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Pizza"
        self._price = 9
        self._description = "Going Canadian? This pizza with pepperoni, bacon and mushrooms is the way to go"
        self._code = 5

class HotDog(MainCourse):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Hot dog"
        self._price = 6
        self._description = "You'll enjoy every single bite of this hot dog with German sausage and cheese"
        self._code = 6

class Salad(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Ceasar Salad"
        self._price = 7
        self._description = "A classic salad with lettuce, croutons, parmesan cheese and our special dressing"
        self._code = 7

class Dessert(FoodItem):
    def __init__(self) -> None:
        super().__init__()
        self._price = 4

class ArrozConLeche(Dessert):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Arroz con leche"
        self._description = "A traditional dessert made with rice, milk and sugar. You'll love it!"
        self._code = 8
        self._is_traditional = True

class IceCream(Dessert):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Vanilla ice cream"
        self._description = "Even if you're a strawberry lover or a chocolate fan, you'll choose this one as your favorite"
        self._code = 9

class DrinkItem(MenuItem):
    def __init__(self):
        super().__init__()
        self._volume: int = 0
        self._brand: str = ""
    
    def get_volume(self) -> int:
        return self._volume
    
    def get_brand(self) -> str:
        return self._brand

class NonAlcoholic(DrinkItem):
    def __init__(self):
        super().__init__()
        self._brand = "Tata's"

class Water(NonAlcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Water"
        self._price = 1
        self._description = "The most underrated drink"
        self._volume = 600
        self._code = 10

class Juice(NonAlcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Orange juice"
        self._price = 2
        self._description = "We know it's not breakfast time, but it's homemade orange juice..."
        self._volume = 400
        self._code = 11
        self._is_seasonal = True

class Soda(NonAlcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Berry soda"
        self._price = 3
        self._description = "A refreshing soda with a mix of berries. Classic drink for a hot day"
        self._volume = 400
        self._code = 12
        self._is_seasonal = True

class Alcoholic(DrinkItem):
    def __init__(self):
        super().__init__()
        self._alcohol_percentage: float = 0
    
    def get_alcohol_percentage(self) -> float:
        return self._alcohol_percentage

class Beer(Alcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Beer"
        self._price = 7
        self._description = "Local-made beer... the closest you'll get to Germany"
        self._volume = 330
        self._brand = "Bavaria"
        self._alcohol_percentage = 5
        self._code = 13

class Wine(Alcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Wine"
        self._price = 12
        self._description = "Feeling French? The entire Paris will envy you with this wine"
        self._volume = 150
        self._brand = "Chateau Margaux"
        self._alcohol_percentage = 12
        self._code = 14

class Cocktail(Alcoholic):
    def __init__(self):
        super().__init__()
        self._name = "Margarita cocktail"
        self._price = 12
        self._description = "A classic cocktail with tequila, lime juice and triple sec"
        self._volume = 200
        self._brand = "Tata's"
        self._alcohol_percentage = 10
        self._code = 15
        self._is_seasonal = True

class Order:
    def __init__(self) -> None:
        self.__status: str = "Open"
        self.__customer_name: str = ""
        self.__items: list[FoodItem] = []
        self.__total_price: float = 0.0
        self.__tip: float = 0.0
        self.__item_codes: dict = {1: lambda: Empanada(), 2: lambda: CheeseStick(), 3: lambda: Pasta(), 4: lambda: Hamburger(), 5: lambda: Pizza(), 6: lambda: HotDog(), 7: lambda: Salad(), 8: lambda: ArrozConLeche(), 9: lambda: IceCream(), 10: lambda: Water(), 11: lambda: Juice(), 12: lambda: Soda(), 13: lambda: Beer(), 14: lambda: Wine(), 15: lambda: Cocktail()} # * So that a new instance of the classes is created every time an item is added to the order

    def print_menu(self) -> None:
        base_order: Order = Order()
        for i in range(1, 16):
            base_order.add_item(i)
        order_iterator: OrderIterator = OrderIterator(base_order)
        print()
        print("---APPETIZERS---")
        for item in order_iterator:    
            if item.get_code() <= 10:
                print(f"{item.get_code()}. {item.get_name()} | ${item.get_price()}")
                print("    -", item.get_description())

            elif item.get_code() <= 12:
                print(f"{item.get_code()}. {item.get_name()} | ${item.get_price()}")
                print(f"    - {item.get_description()} | brand: {item.get_brand()} | volume:", f"{item.get_volume()} ml")

            elif item.get_code() <= 15:
                print(f"{item.get_code()}. {item.get_name()} | ${item.get_price()}")
                print(f"    - {item.get_description()} | brand: {item.get_brand()} | volume:", f"{item.get_volume()} ml | alcohol percentage: {item.get_alcohol_percentage()}%")

            if item.get_code() == 2:
                print()
                print("---MAIN COURSE---")

            if item.get_code() == 6:
                print()
                print("---SALADS---")

            if item.get_code() == 7:
                print()
                print("---DESSERTS---")

            if item.get_code() == 9:
                print()
                print("---NON-ALCOHOLIC DRINKS---")

            if item.get_code() == 12:
                print()
                print("---ALCOHOLIC DRINKS---")
            
    def add_item(self, item_code: int) -> None:
        self.__items.append(self.__item_codes[item_code]())

    def __calculate_item_discount(self, item: FoodItem, item_amount: int) -> float:
        if (item.get_is_traditional()) and (item.get_is_seasonal()):
            if 0.1 * item_amount <= 0.3:
                return round(0.1 * item_amount, 2)
            else:
                return 0.3
        elif (item.get_is_traditional()) or (item.get_is_seasonal()):
            if 0.05 * item_amount <= 0.2:
                return round(0.05 * item_amount, 2)
            else:
                return 0.2
        else:
            return 0

    def __calculate_subtotal_price(self) -> float:
        sub_total: float = 0
        for item in self.__items:
            sub_total += item.get_price_after_discount()
        return round(sub_total, 2)

    def print_order(self, tip_percentage: float = 0) -> None:
        self.__items.sort(key=lambda x: x.get_code())
        i: int = 0
        j: int = 0
        item_amount: int = 0
        current_item_code: int = 0
        order.__calculate_subtotal_price()
        print()
        print(f"*** {self.__customer_name}'s Tata's order ***")
        print("------------------------------------")
        while i < len(self.__items):
            item_amount = 1
            current_item_code = self.__items[i].get_code()
            j = i
            i += 1
            while (i < len(self.__items)) and (self.__items[i].get_code() == current_item_code):
                item_amount += 1
                i += 1
            i -= 1
            items_discount: int = self.__calculate_item_discount(item=self.__items[i], item_amount=item_amount)
            while i >= j:
                self.__items[i].set_discount(items_discount)
                i -= 1
            items_discount /= item_amount
            i = j + item_amount
            print(f"{item_amount}x", self.__items[i-1].get_name(), "->", self.__items[i-1].get_price(), "each:", f"${item_amount * self.__items[i-1].get_price()}", f"(-{self.__items[i-1].get_discount()}% = {(self.__items[i-1].get_price_after_discount()*item_amount)})") # * i - 1 will still be the last instance of the class in question
        print("------------------------------------")
        subtotal_price: float = self.__calculate_subtotal_price()
        print("Subtotal:", f"${subtotal_price}")
        order.set_tip((tip_percentage/100) * subtotal_price)
        print(f"Tip ({tip}%):", f"${round(self.__tip, 2)}")
        self.__total_price = round(subtotal_price + self.__tip, 2)
        print("Total:", f"${self.__total_price}")
        print()
        print("Thank you for coming to Tata's! We hope to see you soon!")
        print("------------------------------------")

    def get_items(self) -> list[FoodItem]:
        return self.__items

    def set_customer_name(self, customer_name: str) -> None:
        self.__customer_name = customer_name
    
    def set_status(self, status: str) -> None:
        self.__status = status

    def set_tip(self, tip: float) -> None:
        self.__tip = tip

class OrderIterator():
    def __init__(self, order: Order) -> None:
        self.__items: list[FoodItem] =  order.get_items()
        self.__index: int = 0
        self.__next: FoodItem = list[0]

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            self.__next = self.__items[self.__index]
            self.__index += 1
            return self.__next
        except IndexError:
            print("*Iteration stopped*")
            raise StopIteration

if __name__ == "__main__":
    try:
        print("🎉🎉 Welcome to Tata's!! 🎉🎉")
        print("What's your name?")
        valid_name: bool = False
        while valid_name == False:
            try:
                customer_name = input()
                if not customer_name.isalpha():
                    raise ValueError("Invalid name")
            except ValueError as e:
                print(e)
            else:
                valid_name = True
        print("A pleasure to meet you {}".format(customer_name))
        print("What would you like to order today?")

        order: Order = Order()
        order.set_customer_name(customer_name)
        order.print_menu()
        done_ordering: bool = False
        print("Please enter the number of the item you want to order. To finish your order type non-numerical characters")
        while not done_ordering:
            try:
                item_code = input()
                if item_code.isalpha():
                    done_ordering = True
                    break
                if int(item_code) not in range(1, 16, 1) or not item_code.isdigit():
                    print(item_code not in range(1, 16), not item_code.isdigit())
                    print(item_code, range(1, 16))
                    raise ValueError("Invalid item")
                order.add_item(int(item_code))
            except ValueError as e:
                print(e)
        print("Alright! I'll bring your order right away")

        time = datetime.now()
        # while (datetime.now() - time).seconds < 5:
            # pass
        print("Here is your order! Enjoy your meal!")
        print("I will bring you the bill once you're ready")
        time = datetime.now()
        # while (datetime.now() - time).seconds < 10:
        #     pass
        print("How much would you like to tip? (Please enter the percentage of the total)")
        valid_tip: bool = False
        while valid_tip == False:
            try:
                tip = input()
                if not tip.isdecimal():
                    raise ValueError("Invalid tip")
                if float(tip) < 0:
                    raise ValueError("Invalid tip")
            except ValueError as e:
                print(e)
            else:
                valid_tip = True
        order.print_order(float(tip))
        order.set_status("Closed")
    except KeyboardInterrupt:
        print()
        print("See you later!")
