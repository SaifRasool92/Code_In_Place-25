# defining constant as mars multiple
MARS_MULTIPLE = 0.378

def main():

    #declaring Variable and getting input from user
    earth_weight=int(input("What is our weight on Earth? "))


    #typecasting the input in string to float


     
    #Defining Mars weight calculation formula and assigning variable
    mars_weight=(MARS_MULTIPLE*earth_weight)

    #string concatenation and  concatenation
    print(f"This is your weight on mars {mars_weight}")
if __name__=="__main__":
    main()


