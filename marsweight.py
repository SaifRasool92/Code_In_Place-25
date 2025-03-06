# File: marsweight.py
"""Formula:0.378*weight on earth"""
# we use constants!
MARS_MULTIPLE = 0.378  # variable

def main():


    weight_on_earth_str =input("What is your weight on Earth? ")



    # input() returns a value in string form, get the number out
    weught_eart=float(weight_on_earth_str)


    # More variables is good times when first learning
    weight_on_mars=(    weught_eart* MARS_MULTIPLE)

    # Note the string concatenation!
    print(f"This is weight on mars: {weight_on_mars}")


if __name__ == '__main__':
    main()