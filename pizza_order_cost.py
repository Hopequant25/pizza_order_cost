#Goal: Calculate the total cost of a pizza order (size + toppings + delivery).
#
# ------------ Psuedo Code ------------
#1.Set the pizza prices and the delivery charges
#2.Ask user to input 
#       -the size they want
#        -number of toppings
#       -distance in miles
#3.Calculate the price of the base cost 
#4.Calculate the price of the toppings 
#5.Calculate the delivery fee according to the distance
#6.Calculate the total cost of the pizza order
#7.Display the cost

# ----------- Prices -----------
#
SMALL_BASE_PRICE = 8
LARGE_BASE_PRICE = 12
TOPPING_PRICE = 1
BASE_DELIVERY_FEE = 2
DELIVERY_CHARGE = 5
EXTRA_MILE_CHARGE = 1

# ------ input --------
size = input("Which one do you want? `small` or `large`: ").strip().lower()
topping = int(input("Number of topping?: "))
Distance_in_miles = int(input("What distance do you live away from CBD in miles?: "))
# ------- BASE COST -------
#
if size == "small":
    base_cost = SMALL_BASE_PRICE
elif size == "large":
    base_cost  = LARGE_BASE_PRICE
    print("chose among the two in lower case")
    raise SystemExit
    
# ------------ toppings -------------

toppings_cost = topping * TOPPING_PRICE


# ------------- miles --------------
#
if Distance_in_miles == 0:
    DELIVERY_CHARGE = 0
elif Distance_in_miles <= BASE_DELIVERY_FEE:
    DELIVERY_CHARGE = BASE_DELIVERY_FEE
else:
    extra_miles =Distance_in_miles - BASE_DELIVERY_FEE
    DELIVERY_CHARGE= BASE_DELIVERY_FEE+ extra_miles * EXTRA_MILE_CHARGE


# -----------TOTAL --------------
#
total_cost = base_cost + toppings_cost + BASE_DELIVERY_FEE


print(f"Your pizza costs ${total_cost}")
