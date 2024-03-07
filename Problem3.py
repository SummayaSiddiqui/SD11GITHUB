print()
NumPounds = int(input("Enter the number of pounds: "))
NumOunces = int(input("Enter the number of ounces: "))
print()

WeightInOunces = NumPounds * 16.00
TotalNumOunces = WeightInOunces + NumOunces

ShippingCost = 0.15 * TotalNumOunces

print()
print("The total number of ounces: ", TotalNumOunces)
print("The shipping cost: ", ShippingCost)
print()


