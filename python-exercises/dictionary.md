Dictionary
===

# Exercise 1

Given 3 orders from a customer within a month, which contains product’s name and quantity
in form of dictionary key-value. Create a dictionary to summarize how much the customer
spent on each product. Price list of products, which contains products’ name and price, given
as below.

Input:

```
order_1 = [{‘PowerCore’: 1}, {‘PowerLine’: 1}]
order_2 = [{‘PowerLine’: 2}]
order_3 = [{‘PowerCore’: 1}, {‘PowerPort’: 2}]

price_list = {
    ‘PowerCore’: 790000,
    ‘PowerLine’: 200000,
    ‘PowerPort’: 750000
}
```

Output:

```
result = {
    ‘PowerCore’: 1580000,
    ‘PowerLine’: 600000,
    ‘PowerPort’: 1500000
}
```

# Exercise 2

Given the following order and delivery order, update the order with delivered quantity provided by the delivery order.

```
order = [
    {
        "product": "PowerCore",
        "ordered_qty": 2,
        "delivered_qty": 0
    },
    {
        "product": "PowerLine",
        "ordered_qty": 5,
        "delivered_qty": 0
    },
    {
        "product": "PowerPort",
        "ordered_qty": 3,
        "delivered_qty": 0
    }
]

delivery_order = [
    {
        "product": "PowerCore",
        "delivered_qty": 2
    },
    {
        "product": "PowerLine",
        "delivered_qty": 3
    }
]
```

# Exercise 3

Given the following order

```
order = [
    {
        "product": "PowerCore",
        "ordered_qty": 2,
    },
    {
        "product": "PowerLine",
        "ordered_qty": 5,
    },
    {
        "product": "PowerPort",
        "ordered_qty": 3,
    },
    {
        "product": "PowerCore",
        "ordered_qty": 1,
    },
    {
        "product": "PowerPort",
        "ordered_qty": 1,
    }
]
```

Print out a consolidated order list with each dictionary contain the unique product and total sum by the given order.