def dictfunc1():
    print("Consider the following orders and price list")
    order_1 = [{'PowerCore': 1}, {'PowerLine': 1}]
    print("Order 1 :", order_1)
    order_2 = [{'PowerLine': 2}]
    print("Order 2 :", order_2)
    order_3 = [{'PowerCore': 1}, {'PowerPort': 2}]
    print("Order 3 :", order_3)
    price_list = {'PowerCore': 790000, 'PowerLine': 200000, 'PowerPort': 750000}
    print("Price List :",price_list)

    # Concatenate all orders
    all_orders = order_1 + order_2 + order_3

    # Loop through all items in order to calculate costs
    total_spent = dict()
    for item in all_orders:
        for key in item:
            price = price_list.get(key)
            quantity = item.get(key)
            total = quantity * price
            # if the key in dictionary then update the value
            if key in total_spent.keys():
                total_spent[key] += total
            # if they key is not in dictionary, then add the key and value
            else:
                total_spent[key] = total

    print("Total spent :",total_spent)

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = dictfunc1()


#Output:

#result = {
#    ‘PowerCore’: 1580000,
#    ‘PowerLine’: 600000,
#    ‘PowerPort’: 1500000
#}



