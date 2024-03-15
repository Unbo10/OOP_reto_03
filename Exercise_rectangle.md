# Rectangle class diagram and line exercise

To make this exercise five classes were created: Point, Segment (originally asked as "Line" in the requirements), Line (extra class), Rectangle and Square. Point illustrates composition at its best as all the other classes have at least an object of Point. Segment and Line together show an aggregation relation and even polymorphism with the method ``determine_type()``, while the Rectangle class uses all the other classes (except Square) inside its methods. Lastly, Square is the perfect example of inheritance as it is initialized calling the initializer of Rectangle. The [code implementation](./exercise_rectangle_composition.py) can be executed and it will create at least an object of each class and try the most interesting methods of each.

<br>

```mermaid

classDiagram
direction TB

    class Point {
        + float x
        + float y
        - __init__(float given_x, float given_y)
        - move(): void
        - reset(): void
        - compute_distance(Point): float
    }

    class Line {
        + Point start
        + Point end
        + float slope
        + float x
        + float b
        + str type
        - __init__(Point, Point)
        # determine_type(): void
    }
    Line "1" *-- "2" Point: has

        class Segment {
        + Point start
        + Point end
        + Line associated_line
        + str type
        + float length
        + float slope
        + float b
        - __init__(Point, Point)
        # determine_type()
        - compute_length()
        - compute_slope()
        - compute_x_cross()
        - compute_y_cross()
        - descretize_segments()
    }
    Segment "1" *-- "2" Point: has
    Segment "1" o-- "1" Line: has a line associated

    class Rectangle {
        + float width
        + float height
        + Point center
        - __init__(method, *args)
        # compute_area()
        # compute_perimeter()
        # compute_interference_point(Point)
        # compute_interference_line(Line)
        # compute_interference_segment(Segment)
    }
    Rectangle "1" -- "*" Line: can be intercepted by
    Rectangle "1" -- "*" Segment: can be intercepted by
    Rectangle "1" *-- "1" Point: has a
    Rectangle "1" <|-- "1" Square: is a

    class Square {
        - __init__(method, *args)
    }
    Square "1" *-- "1" Point: has a
    
```

