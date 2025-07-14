def calculate_bmi(weight_kg, height_m):
    if height_m <=0:
        return None
    else:
        bmi =  weight_kg / (height_m ** 2)
        return  round(bmi,2)

    
def classify_bmi(bmi_value):
    
    if bmi_value is None:
       return "Invalid input"
    elif bmi_value < 18.5:
       return "you are Underweight please take good food"
    elif bmi_value > 18.5 and bmi_value <24.9:
        return "you are Normal weight keep it up"  
    elif bmi_value > 25 and bmi_value <29.9: 
        return "you are Overweight please do exercise "
    else:
        return "you are Obese please consult doctor"      
    

def get_weight():
   while True:
        try:
             weight_kg = float(input("please enter weight in kg"))
             if weight_kg >0:
                return weight_kg
             else:
                print("weight must be in positive number..")
        except ValueError:
               print("❌ Invalid input. Please enter a number.")
         
def get_height():
    while True:
        unit = input("you want to enter height in 'ft' or 'meter' select one unit")
        if unit == 'ft':
            prompt = ("please enter height in feet only")
            factor =0.3048
        elif unit == 'meter':
            prompt = ("please enter height in meter only")
            factor = 1
        else:
            print("please select valid unit of height") 
            continue

        try:
            value = float(input(prompt))
            if value >0:
                return value * factor   
            else :
                print("height must be greater then zero")
        except ValueError:
            print("invalid input please enter valid height")  






def main():
    print("\nwelcome to BMI CALCULATOR")
    name = input("please enter you name")
    height = get_height()
    weight = get_weight()
    bmi = calculate_bmi(weight,height)
    category = classify_bmi(bmi)

    print("\n=== Results ===")
    print(f"Hello {name}, your BMI is: {bmi:.2f}")
    print(f"Health Category: {category}")
    print("=========================")

if __name__ == "__main__":
    main()


         

