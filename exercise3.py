from xmlrpc.client import boolean

cup_of_water = 75.5
#max cup_of_water value = 100
#min cup_of_water value = 0
var1 = "Full"
var2 = "Empty"
var3 = "Half Full"
if cup_of_water > 50:
    print(var1)
elif cup_of_water == 50:
    print(var3)
else:
    print(var2)
