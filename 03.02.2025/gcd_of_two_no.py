def gcd (num1 : int,num2 : int) -> int :
    if(num1 ==0 or num2== 0) :
        return 0
    elif (num1 == num2) :
        return num1
    else :
        for i in range(1 , max(num1 , num2) +1 ) :
            if num1 %i ==0 and num2 %i ==0 :
                gcd_value =i
        return gcd_value;
        
a = int(input("Please enter number1: "))
b = int(input("Please enter number2: "))
gcd_value =1
print("The GCD of the numbers is:", gcd(a, b))