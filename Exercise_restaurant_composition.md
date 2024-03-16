# Restaurant: 

```mermaid

classDiagram
direction TB

class Customer {
    +String name
    +float wallet
    +drink(Beverage)
    +eat(Food)
    -reject()
    -drop()
}

class Waiter {
    -String name
    -float tips
    +take_order(Customer): Order
    +deliver_order(): void
    +bring_bill(): ~List~
    +add_tip(float tip): void
}

class Order {
    +List~MenuItem~ order_items
    +float discount
    +apply_discount(order_items): float
}

Order "1" o-- "*" MenuItem : has a

class MenuItem {
    +String name
    +float price
    +calculate_price(): float
}
MenuItem "0..n" <|-- "0..n" LiquidItem: is a
MenuItem "0..n" <|-- "0..n" FoodItem: is a
MenuItem <|-- AllInOne: is a

class LiquidItem {
    +bool is_alcoholic
    +bool is_carbonated
    +bool ice
    +bool refill
    +bool age_restriction
    +Date expiration_date
    +String brand
    +String flavor
    +float volume
}

LiquidItem "0..n" <|-- "0..n" Alcoholic: is a
LiquidItem "0..n" <|-- "0..n" NonAlcoholic: is a

class Alcoholic {
    +float alcohol_percentage
}

Alcoholic <|-- Cocktail
Alcoholic <|-- Beer
Alcoholic <|-- Wine

class Cocktail {
    +bool is_highball
    +<String> spirits_mixed
}

class Beer {
    +String color
}

class Wine {
    +int year_sealed
    +String type
    +String strain
}

class NonAlcoholic {
    +bool is_homemade
}

NonAlcoholic "1" <|-- "1" Juice: is a
NonAlcoholic "1" <|-- "1" Water: is a
NonAlcoholic "1" <|-- "1" TemperanceDrink: is a

class Juice {
    +~String~ fruits
    -bool is_fresh
}

class Water {
    +bool is_tap
    -String definition
}

class TemperanceDrink {
    +String drink_imitated
}

class FoodItem {
    +bool is_fried
    +bool is_vegan
    +bool is_vegetarian
    +bool is_spicy
    +bool is_glutenFree
    +bool is_chef_suggestion
    +bool nuts
    -int people_size
    -float price
    -float discount
    -String origin 
    -String temperature
    -List~String~ shareable_ingredients
    -List~String~ secret_ingredients

    +get_shareable_ingredients(): ~String~
    +set_shareable_ingredients(Waiter, String password, ~String~): ~String~
    +get_secret_ingredients(Waiter, String password): ~String~
    +set_secret_ingredients(Waiter, String password, ~String~): void
    +get_ingredients(): ~String~
    +set_ingredients(Waiter, String password, ~String~)
    +get_discount(): float
    +set_discount(Waiter, String password): float
}
FoodItem "0..n" <|-- "0..n" Appetizer: is a
FoodItem "0..n" <|-- "0..n" MainCourse: is a
FoodItem "0..n" <|-- "0..n" Dessert: is a

class Appetizer {
    +get_discount(): float
    -calculate_discount(): float
}

Appetizer <|-- Soup: is an

class Soup {
    -bool texture_smooth
    +get_texture()
    +set_texture(Waiter, String password, String texture)
}

class MainCourse {
    +calculate_discount(~MainCourse~): float
}
MainCourse <|-- Pasta: is a
MainCourse <|-- Junk: is a
MainCourse <|-- Salad: is a
MainCourse <|-- Traditional: is a

class Pasta {
    -String sauce
    -String pasta_type
    +get_sauce_and_type()
    +set_sauce_and_type()
}

class Salad {
    +bool warm_ingredients
    +bool only_greens
    +bool local_ingredients
    +float local_discount
    +get_discount(): float
    +calculate_discount(): float
    +set_discount()
}

class Junk {
    +String sauce
    +get_sauce()
    +set_sauce()
}

class Traditional {
    +float discount
}

Junk <|-- Pizza: is a
Junk <|-- Hamburger: is a
Junk <|-- HotDog: is a

class Pizza {
    +<String> toppings
    +String crust
}

class Hamburger {
    +bool double_patty
    +bool vegeatables
    +String cheese
}

class HotDog {
    +String sausage_type
    +String bread_type
}

class Dessert {
    +bool 
    +int preparation_time
}

class AllInOne {
    -LiquidItem drink
    -Appetizer appetizer
    -MainCourse main_course
    -Dessert dessert
    +get_items()
    +get_ingredients()
    +set_items(Waiter, String: password)
    +set_ingredients()
}
