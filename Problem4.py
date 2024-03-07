print()
SalesName = input("Enter the salesperson name: ")
TripLocation = input("Enter the trip location: ")
print()
NumDays = int(input("Enter the number of days: "))
NumKilo = input("Enter the number of kilometers: ")
NumKilo = int(NumKilo)

PerDiemAmt = NumDays * 56.00

NumNights = NumDays - 1
LodgingAmt = (NumNights) * 125.00
MilAmt = NumKilo * 0.24

TotalClaim = PerDiemAmt + LodgingAmt +MilAmt
HST = (PerDiemAmt + LodgingAmt) * 0.15
ClaimTotal = TotalClaim + HST

print()
print("Salesperson name: ", SalesName)
print("TripLocation:   ", TripLocation)
print("Number of days:   ", NumDays)
print("Number of kilometers:  ", NumKilo)

print()
print("Per Diem amount:   ", PerDiemAmt)
print("Lodging amount:  ", LodgingAmt)
print("Mileage amount:  ", MilAmt)


print()
print("Total claim:  ", TotalClaim)
print("HST:     ", HST)
print("Claim total:    ", ClaimTotal)
