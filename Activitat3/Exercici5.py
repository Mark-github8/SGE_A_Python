num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
par = 0
inpar = 0
for x in num:
    if x % 2 == 0:
        par = par + x
    else:
        inpar = inpar + x
print (f"Par: {par}")
print (f"Inpar: {inpar}") 