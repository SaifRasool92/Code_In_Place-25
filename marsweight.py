MARS_MULTIPLE = 0.378

def main():
    Earth_weight_str=input("What is your weight on Earth? ")
    earth_weight=float(Earth_weight_str)
    mars_weight=(earth_weight*MARS_MULTIPLE)
    print(f"This is equivalent weight on mars {mars_weight}")

if __name__ == '__main__':
    main()