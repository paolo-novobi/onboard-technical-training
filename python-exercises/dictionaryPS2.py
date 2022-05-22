def dictfunc2():
    order = [{"product": "PowerCore","ordered_qty": 2,"delivered_qty": 0},
             {"product": "PowerLine","ordered_qty": 5,"delivered_qty": 0},
             {"product": "PowerPort","ordered_qty": 3,"delivered_qty": 0}]

    print("The placed order :",order)
    delivery_order = [{"product": "PowerCore","delivered_qty": 2},
                      {"product": "PowerLine","delivered_qty": 3}]

    print("\nThe delivery made :",delivery_order)
    for delivery in delivery_order:
        product = delivery.get("product")
        delivered_qty = delivery.get("delivered_qty")
        for items in order:
            if (items.get('product') == product):
                items['delivered_qty'] += delivered_qty
                break

    print("\nThe updated order :", order)

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = dictfunc2()
