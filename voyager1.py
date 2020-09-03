
days_str = input("Number of days after 9/25/09: ")
days_int = int(days_str)
km_per_mile = 1.609344
mile_per_au = 92955887.6

# Býr til breytu fyrir hverja mælieiningu með vegalengdinni sem var komin 9/25/09
base_distance_miles = 16637000000
base_distance_km = base_distance_miles * km_per_mile
base_distance_au = base_distance_miles / mile_per_au

# Býr til breytu fyrir hverja mælieiningu sem inniheldur vegalengdina sem skipið ferðast á dag 
miles_per_day = 38241 * 24
km_per_day = miles_per_day * km_per_mile
au_per_day = miles_per_day / mile_per_au

#Býr til breytu sem inniheldur heildar vegalengd eftir hversu marga daga sem inputtið var. Ein breyta fyrir hverja mælieiningu
miles_from_sun = base_distance_miles + miles_per_day * days_int
km_from_sun = round(base_distance_km + km_per_day * days_int)
au_from_sun = round(base_distance_au + au_per_day * days_int)


print("Miles from the sun: " +  str(miles_from_sun))
print("Kilometers from the sun: " + str(km_from_sun))
print("AU from the sun: " + str(au_from_sun))
