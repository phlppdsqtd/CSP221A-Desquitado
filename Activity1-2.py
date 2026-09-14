orders = [
    ("Laptop", 2, 350),
    ("Mouse", 5, 20),
    ("Monitor", 3, 220),
]

def add_order(orders_list, item, quantity, price):
    orders_list.append((item, quantity, price))

add_order(orders, "Desk", 2, 300)
add_order(orders, "Keyboard", 4, 30)

high_value_items = []
overall_total_cost = 0

for item, quantity, price in orders:
    total_cost = quantity * price
    if total_cost > 500:
        high_value_items.append(item)
        overall_total_cost += total_cost

print("High-Value Items:", high_value_items)
print("Overall Total Cost:", overall_total_cost)