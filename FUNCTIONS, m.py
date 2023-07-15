        determineIdealPricing(ranchersProduce, marketPrices):
if marketPrices is empty:
    return "No market prices available."
else:
    idealPrice = average(marketPrices)
    if ranchersProduce is in high demand:
        idealPrice *= 1.2  # 20% markup
    else if ranchersProduce is in low demand:
        idealPrice *= 0.8  # 20% discount
    if idealPrice > ranchersCostPrice:
        return "Set the selling price as: " + idealPrice
    else:
        return "The selling price should cover at least the cost price."

        determineChosenTransportation(ranchersProduce, transportationOptions):
if transportationOptions is empty:
    return "No transportation options available."
else:
    chosenTransportation = transportationOptions[0]
    for option in transportationOptions:
        if option.deliveryTime < chosenTransportation.deliveryTime:
            chosenTransportation = option
    if chosenTransportation is not null:
        return "The chosen transportation method is: " + chosenTransportation.name
    else:
        return "No suitable transportation method found."