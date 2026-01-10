def get_delivery_status(delivery):
    """
    delivery is a dictionary like:
    {
        "delivered": True or False,
        "problem": True or False
    }
    """

    # Edge case: missing data
    if "delivered" not in delivery or "problem" not in delivery:    
        return "blocked"

    if delivery["problem"]: 
        return "blocked" 

    if delivery["delivered"]:
        return "done"

    return "open"


delivery1 = {"delivered": True, "problem": False}   # Package arrived
delivery2 = {"delivered": False, "problem": True}   # Truck broke down
delivery3 = {"delivered": False, "problem": False}  # Still on the way
delivery4 = {"delivered": True, "problem": True}    # Delivered but damaged

print("Delivery 1: " + get_delivery_status(delivery1))  # done
print("Delivery 2: " + get_delivery_status(delivery2))  # blocked
print("Delivery 3: " + get_delivery_status(delivery3))  # open
print("Delivery 4: " + get_delivery_status(delivery4))  # blocked