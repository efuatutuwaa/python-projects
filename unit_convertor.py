convert_from = input("Enter Starting Unit of Measurement(inches, feet, or yards):")
convert_to = input("Enter Unit of Measurement to Convert to(inches, feet, or yards):")

if convert_from.lower() in ['inches', 'inch', 'in']:
    number_of_inches = int(input("Enter Starting Measurement in Inches:"))
    if convert_to.lower() in ['feet', 'ft']:
        print(number_of_inches, 'inches =', number_of_inches / 12, 'feet')
    elif convert_to.lower() in ['yards', 'yard', 'yd', 'yds']:
        print(number_of_inches, 'inches =', number_of_inches / 36, 'yards')
    else:
        print("Please enter either 'inches, 'feet', or 'yards' in the Unit of Measurement to Convert")
elif convert_from.lower() in ['feet', 'ft']:
    number_of_feet = int(input("Enter Starting Measurement in Feet:"))
    if convert_to.lower() in ['inches', 'in']:
        print(number_of_feet, 'feet =', number_of_feet * 12, 'inches')
    elif convert_to.lower() in ['yards', 'yard', 'yd', 'yds']:
        print(number_of_feet, 'feet =', number_of_feet / 3, 'yards')
    else:
        print("Please enter either 'inches, 'feet', or 'yards' in the Unit of Measurement to Convert")
elif convert_from.lower() in ['yards', 'yard', 'yd', 'yds']:
    number_of_yards = int(input("Enter Starting Measurement in Yards:"))
    if convert_to.lower() in ['inches', 'in']:
        print(number_of_yards, 'yards =', number_of_yards * 36, 'inches')
    elif convert_to.lower() in ['feet', 'ft']:
        print(number_of_yards, 'yards =', number_of_yards * 3, 'feet')
    else:
        print("Please enter either 'inches, 'feet', or 'yards' in the Unit of Measurement to Convert")
else:
    print("Please enter either 'inches, 'feet', or 'yards' for the starting Unit of Measurement")
