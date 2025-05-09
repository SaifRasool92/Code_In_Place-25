
"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    earth_weight=float(input("Enter your weight on Earth? "))
    planet=("Enter your Planet? ")
    if planet==MERCURY:
        gravity_constant=MERCURY_GRAVITY
    elif planet==VENUS:
        gravity_constant=VENUS_GRAVITY_GRAVITY
    elif planet==MARS:
        gravity_constant=MARS_GRAVITY_GRAVITY
    elif planet==SATURN:
        gravity_constant=SATURN_GRAVITY
    elif planet==URANUS:
        gravity_constant=URANUS_GRAVITY
    elif planet==NEPTUNE:
        gravity_constant=NEPTUNE_GRAVITY
    else:
        gravity_constant=EARTH_GRAVITY


Planet_weight=(gravity_constant * earth_weight)
rounded_planetary_weight = round(planetary_weight, 2)
print(f"The weight on {planet} is : {rounded_planetary_weight}")

if __name__ == "__main__":
    main()
   