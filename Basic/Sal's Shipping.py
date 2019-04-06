shipping_cost_premium = 125.00
def cost_of_ground_shipping(weight):
    if weight <= 2:
        price_per_pound = 1.50
    elif 2 < weight <= 6:
        price_per_pound = 3.00
    elif 6 < weight <= 10:
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75
    return 20 + (weight * price_per_pound)

def cost_of_drone_shipping(weight):
    if weight <= 2:
        price_per_pound = 4.50
    elif 2 < weight <= 6:
        price_per_pound = 9.00
    elif 6 < weight <= 10:
        price_per_pound = 12.00
    else:
        price_per_pound = 14.25
    return (weight * price_per_pound)

def cheapest_cost_of_shipping(weight):
    ground = cost_of_ground_shipping(weight)
    drone = cost_of_drone_shipping(weight)
    premium = shipping_cost_premium
  
    if ground < drone and ground < premium:
        method = "ground shipping"
        cost = ground
    elif drone < ground and drone < premium:
        method = "drone shipping"
        cost = drone
    else:
        method = "premium shipping"
        cost = premium
    print("The cheapest option %s and cost %.2f" %(method,cost))

cheapest_cost_of_shipping(4.8)
cheapest_cost_of_shipping(41.5)