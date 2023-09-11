    
def arctan():
    def subarctan(n,k):
        arctan_value = 0
        for i in range(1,k+1):
            term = (((-1)**(i-1))*(n**(2*i-1)))/(2*i-1)
            arctan_value += term
        return arctan_value
    x = float(input("What's the number?"))
    y = int(input("What's the number of terms in the taylor series?"))

    print("The value of the arctan of the given number is:", subarctan(x,y))


def epower():
    def factorial(s):
        if s == 0:
            return 1
        else:
            return s*factorial(s-1)
    def subepower(n,t):
        e_value = 0
        for i in range(1,t+1):
            term = n**(i-1)/factorial(i-1)
            e_value += term
        return e_value
    x = float(input("What's the power of e?"))
    y = int(input("How many terms are in the taylor series?"))
    print("The value is:",subepower(x,y))

def sin():
    def factorial(s):
        if s == 0:
            return 1
        else:
            return s*factorial(s-1)
    def subsin(n,t):
        sin_value = 0
        for i in range(1,t+1):
            term = ((n**(2*i-1))*((-1)**(i-1)))/(factorial(2*i-1))
            sin_value += term
        return sin_value
    print("The value of the sine is:",subsin(float(input("What's the angle/radian?")),int(input("What's the number of terms in the taylor series?"))))

def cos():
    def factorial(s):
        if s == 0:
            return 1
        else:
            return s*factorial(s-1)
    def subcos(n,t):
        cos_value = 0
        for i in range(1,t+1):
            term = (((-1)**(i-1))*(n**(2*i-2)))/(factorial(2*i-2))
            cos_value += term
        return cos_value   
    print("The cos of the given number is",subcos(float(input("What's the radian?")),int(input("What's the number of terms?"))))

def tan():
     def factorial(s):
        if s == 0:
            return 1
        else:
            return s*factorial(s-1)
     def subcos(n,t):
        cos_value = 0
        for i in range(1,t+1):
            term = (((-1)**(i-1))*(n**(2*i-2)))/(factorial(2*i-2))
            cos_value += term
        return cos_value 
     def subsin(n,t):
        sin_value = 0
        for i in range(1,t+1):
            term = ((n**(2*i-1))*((-1)**(i-1)))/(factorial(2*i-1))
            sin_value += term
        return sin_value
     x = float(input("What's the radian?"))
     y = int(input("What's the number of terms in the taylor series?"))

     print("The value of tan is equal to:",(subsin(x,y))/subcos(x,y))

def cosh():
        def subepower(n,t):
            def factorial(s):
                if s == 0:
                    return 1
                else:
                    return s*factorial(s-1)
            e_value = 0
            for i in range(1,t+1):
                term = n**(i-1)/factorial(i-1)
                e_value += term
            return e_value
        x = float(input("What's the number?"))
        y = int(input("What's the number of terms in the taylor series?"))
        print("The value of cosh for the given number is:", 0.5*(subepower(x,y) + subepower(-x,y)))

def sinh():
    def epower(n,t):
        def factorial(s):
            if s == 0:
                return 1
            else:
                return s*factorial(s-1)
        e_value = 0
        for i in range(1,t+1):
            term = n**(i-1)/factorial(i-1)
            e_value += term
        return e_value
    x = float(input("What's the number?"))
    y = int(input("What's the number of terms in the taylor series?"))
    print("The value of sinh for the given number is:", 0.5*(epower(x,y)-epower(-x,y)))

def log():
        def sublog(n,t):
            z = n-1
            log_value = 0
            for i in range(1,t+1):
                term = (((-1)**(i-1))*(((z/128)**(i))))/(i)
                log_value += term
            return log_value
        print("The value of log is:",2.10720996965+sublog(float(input("What's the number?")),int(input("What's the number of terms in the taylor series?"))))

def varpower():
     a = float(input("What's the value of the power?"))
     b = float(input("What's the value of the base?"))
     c = int(input("What's the number of terms in the taylor series?"))
     def subvarpower(a,b,c):
         def sublog(n,t):
            z = n-1
            log_value = 0
            for i in range(1,t+1):
                term = (((-1)**(i-1))*(((z/128)**(i))))/(i)
                log_value += 2.10720996965+term
            return log_value
         def factorial(s):
             if s == 0:
                 return 1
             else:
                 return s*factorial(s-1)
         varpower_value = 0
         for i in range(1,c+1):
             term = (((float(sublog(b,40))*a)**(i-1))/(factorial(i-1)))
             varpower_value += term
         return varpower_value
     print("The answer is:",subvarpower(a,b,c))

def cotan():
    def factorial(s):
        if s == 0:
            return 1
        else:
            return s*factorial(s-1)
    def cot():
        t = int(input("Please enter the number of terms in the taylor series. "))
        n = float(input("Please enter the radian. "))
        def cos(x,y):
            cos_value = 0
            for i in range(1,y+1):
                term = (((-1)**(i-1))*((x)**(2*i-2)))/factorial(2*i-2)
                cos_value += term
            return cos_value
        def sin(x,y):
            sin_value = 0
            for i in range(1,y+1):
                term = (((-1)**(i-1))*((x)**(2*i-1)))/factorial(2*i-1)
                sin_value += term
            return sin_value
        cot_value = cos(n,t)/sin(n,t)
        print("The value of the cotangent of the given radian is : ",cot_value)
    cot()


