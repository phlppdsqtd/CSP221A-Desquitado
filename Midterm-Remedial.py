import pandas as pd

raw_rows = [
    {"name": "Widget", "price": 12.50, "quantity": 40},
    {"name": "Gadget", "price": 8.00, "quantity": 15},
    {"name": "Gizmo", "price": -5.00, "quantity": 10},
    {"name": "Doohickey", "price": 3.25, "quantity": -2},
    {"name": "Thingamajig", "price": 0, "quantity": 5},
    {"name": "Contraption", "price": 15.00, "quantity": 0},
    {"name": "Sprocket", "price": 6.75, "quantity": 25},
]

df = pd.DataFrame(raw_rows)
print(df)