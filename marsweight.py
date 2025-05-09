# defining constant as mars multiple

MARS_MULTIPLE = 0.378

def main():

   # getting input from user and storing in variable

    #declaring Variable and getting input from user
    earth_weight=input("What is our weight on Earth? ")

    #changing type of the string(taking as input) to float is called typecasting

    #Defining Mars weight calculation formula and storing value in variable mars_weight

    #printing string concatenation (combining two strings into one)



    #typecasting the input in string to float
    MARS_weight=int(earth_weight)

 
    #Defining Mars weight calculation formula and assigning variable
    mars_weight=(MARS_MULTIPLE*MARS_weight)

    #string concatenation and  concatenation
    print(f"This is your weight on mars {mars_weight}")
if __name__=="__main__":
    main()


#INPUT 12
#OUTPUT 4.42


