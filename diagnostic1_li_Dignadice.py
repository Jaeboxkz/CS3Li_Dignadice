def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping = 15
    elif shipping_speed == "overnight":
        shipping = 25
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping = 0
    elif shipping_speed == "standard" and cart_total < 100:
        shipping = 10
    else:
        print("ERROR")
        shipping = 0
    total = shipping + cart_total
    return total
print(calculate_checkout(10000,"express"))
print(calculate_checkout(100, "standard"))
print(calculate_checkout(99, "standard"))