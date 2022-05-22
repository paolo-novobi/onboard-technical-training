def dictfunc3():
    order = [{"product": "PowerCore","ordered_qty": 2,},
             {"product": "PowerLine","ordered_qty": 5,},
             {"product": "PowerPort","ordered_qty": 3,},
             {"product": "PowerCore","ordered_qty": 1,},
             {"product": "PowerPort","ordered_qty": 1,}]
    print("Order list: ",order)
    consolidated_order = dict()
    for item in order:
        product = item.get("product")
        quantity = item.get("ordered_qty")
        if product in consolidated_order.keys():
            consolidated_order[product] += quantity
        else:
            consolidated_order[product] = quantity
    
    print("\nConsolidated order :",consolidated_order);

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = dictfunc3()
