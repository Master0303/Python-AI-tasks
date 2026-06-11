#Q1
def calculator(num1,num2,operation):
    if operation == "*":
        result=num1 * num2
        return result
    elif operation == "+" :
        result=num1 + num2
        return result
    elif operation == "/":
        result=num1 / num2
        return result
    elif operation == "-":
        item=num1 - num2
        return result
    else:
        return "invalid operation"

print(calculator(50,20,"+"))

#Q2
def build_profile(name,country="unkown",**info):
    print(f"Welcome {name} from {country}\nYour extra info:")

    for i in info:
        print(i,":",info[i])

dic={
    "age":36,
    "skills":["ML","C++","Python","Javascript"],
    "GPA":4.5
}
build_profile("Ahmed",**dic)

#Q3
counter=0
def increment_counter():
    global counter
    counter+=1
    return counter

def local_counter():
    counter=10
    return counter

print(f'''This is the global counter before the addition:{counter}
     This is the increment counter:{increment_counter()}
    This is the global counter after the addition in the increment function:{counter}
    This is the local counter:{local_counter()}''')

#Q4
def countdown(n):
    if n<=0:
        print("Blastoff!")
    else:
        print(n) , countdown(n-1)
    
countdown(7)

#Q5
square=lambda x: x**2
print(square(6))
is_even=lambda n: print("True") if n%2==0 else  print("False")
is_even(7)

#Q6
print(max([15, 8, 99, 23]))
print(abs(-42))
x=list(range(2,11,2))
print(x)
print("Python","is","awesome",sep="-")

#Q7
salaries = [2000, 3500, 4000, 5500]
bonus=map(lambda add: add*1.1,salaries)
print(list(bonus))

#Q8
ages = [15, 22, 17, 30, 45, 12, 18]
age_verification=list(filter(lambda x:x>=18,ages))
print(age_verification)

#Q9
data = [("Ahmed", 45), ("Sara", 85), ("Ali", 90), ("Omar", 30)]
_pass=list(filter(lambda x:x[1]>=50,data))#[('Sara', 85), ('Ali', 90)]
name=list(map(lambda y:y[0],_pass))#['Sara', 'Ali']
for student in name:
    print(f'"Congratulations {student}!"')
