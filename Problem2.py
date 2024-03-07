print()
SourceLoc = input("Enter the source location")
CallDestination = input("Enter the call destination")
print()
NumMinutes = int(input("Enter the number of minutes"))

CallCost = 1.3 + (0.12 * (NumMinutes - 1))

print()
print("the source location ", SourceLoc)
print("the call destination ", CallDestination)
print("the number of minutes ",NumMinutes)

print("the call of the cost ",CallCost)
    