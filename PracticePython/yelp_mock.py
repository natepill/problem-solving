#!/usr/local/bin/python3
import sys, json;
data = json.load(sys.stdin)

MEAL_PRICE = 10
MAXIMUM_DISCOUNT = 0.3

def get_meal_price(customer_email: str) -> float:

    discount = 1.0
    for visit in data:
        if discount == 0.7:
            break
        if visit.email = customer_email:
            discount -= 0.1

    return MEAL_PRICE*discount


assert(get_meal_price("bashard5@sun.com") == 9.0)
assert(get_meal_price("nlohana@yelp.com") == 10.0)
assert(get_meal_price("jsirett2@csmonitor.com") == 7.0)
