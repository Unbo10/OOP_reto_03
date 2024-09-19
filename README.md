# Challenge 7 (Restaurant)

Although the goal was to reuse challenge 3's code, mine was pretty bad written. In fact, when I tried to read it again, I couldn't even understand it (I took too much time doing the class diagram and so the code was wrote almost mindlessly to fulfill the deathline).

In consequence, I did everything from scratch, taking only from challenge 3 the classes and the methods of the Order class. However, I think it turned decently acceptable, and most importantly, it's functional and doesn't have any bugs or logic errors (some of which the other one did have). Plus, a more concise class diagram was elaborated [here](ClassDiagram.md).

Now, going back to the matter, in the challenge 7 we were asked to create a class that initialized iterator objects of the `Order()` class, that is, a class that allowed looping and implemented the two main methods of an iterator: `__iter__` and `__next__`. The first returns `self` (since any object of this new class should be an iterator), whilst the second one returns a value depending on the variables inside of its scope (it's a method with acces to the object's attributes, which allows it to 'remember' the previous iteration).

The class's identifier is `OrderIterator`, and its implementation is the following one:

```py

class OrderIterator():
    def __init__(self, order: Order) -> None:
        self.__items: list[FoodItem] =  order.get_items()
        self.__index: int = 0

    def __iter__(self) -> "OrderIterator":
        return self
    
    def __next__(self) -> FoodItem:
        try:
            next: FoodItem = self.__items[self.__index]
            self.__index += 1
            return next
        except IndexError:
            raise StopIteration

```

as you can see, it is initalized with an order (an object of Order) and stores the order's items in a private attribute, as well as the current iteration or index. In the `__next__` method, it raises a `StopIteration` exception to stop the iteration when in a for loop, a list comprehension or any sort of iteration process handled by Python.

It is used in the `print_menu()` method of an `Order`'s object as follows:

```py

    def print_menu(self) -> None:
        base_order: Order = Order()
        for i in range(1, 16):
            base_order.add_item(i)
        order_iterator: OrderIterator = OrderIterator(base_order)
        print()
        print("---APPETIZERS---")
        for item in base_order:    
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

```

Note that all the items are being printed using the for loop `for item in base_order`, which entails the use of the an `OrderIterator` object because the `__iter__` method defined in class `Order` is:

```py

    def __iter__(self):
        return OrderIterator(self)

```

this succsefully returns an iterator of the current order, making it possible to print the menu in the terminal ([try it out!](restaurant_exercise.py)).

Have a nice day! :D

