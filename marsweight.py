mar_multiple=0.378
def main():
    Earth_weight_str= input("What is you  weight on Earth? ")
    Earth_weigth=float(Earth_weight_str)

    Mars= (Earth_weigth * mar_multiple)
    print("Your equivalent weight on Mars is: "+ str(Mars))
# declare input

if __name__=="__main__":
    main()

