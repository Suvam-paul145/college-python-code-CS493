def gcd(a,b):
    if a == b :
        return a
    else:
        if a>=2*b:
            for i in range(2,b+1):
                if(a % i ==0 & b % i ==0):
                    gcd = i
            return gcd
        else:
            if b>=2*a:
                for i in range(2,a+1):
                    if(a % i ==0 & b % i ==0):
                        gcd = i
                return gcd

print("Enter two no for finding LCM and GCD ")
a = int(input("Enter first no: "))
b = int(input("Enter second no: "))
print("The GCD is: ", gcd(a,b))
print("The LCM is:", a*b/gcd(a,b)) 
        