shours=input("Enter hours:")
try:
    fhours=float(shours)
except:
    print("Enter hours in numeric value")

srate_per_hour=input("Enter rate per hour:")
try:
    frate_per_hour=float(srate_per_hour)
except:
    print("Enter rate per hour in numeric value")
    
if fhours > 40 :
    print("Total wages=",((fhours-40)*frate_per_hour*1.5)+(40*frate_per_hour))
else :
    print("Total wages=",fhours*frate_per_hour)