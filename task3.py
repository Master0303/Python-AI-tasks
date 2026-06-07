#Q1
print("Please enter your name")
name=input().title().strip()
print("Please enter your birth year")
birth_year=int(input())
print("Please enter your GPA")
GPA=float(input())
age=2026-birth_year
print(f"Your name is {name}, Yous are {age} years old, your GPA={GPA}")

#Q2
balance=500
balance+=200
print(f"Your new balance after deposit={balance}")
balance-=150
print(f"Your new balance after your last withdraw={balance}")
balance*=2
print(f"Congrats you won after your last withdraw 2x multiplier on your balance your new balance={balance}")
print(f"Is the balance equal to 1100 ({balance==1100})")
print(f"Is the balance greater than 500 ({balance>500})")
print(f"Is the balance not equal to 0 ({balance!=0})")

#Q3
has_ticket = True
is_vip = False
age = 17
print(f"Can the person enter the general area ({has_ticket and age>=18})")
print(f"Can the person enter the VIP area ({has_ticket and is_vip})")
print(f"Does the person get a youth discount ({age<18 or is_vip})")
print(f"Is the person NOT a VIP ({not is_vip})")

#Q4
print("Please enter your score and it should be from 0 to 100")
score=int(input())
if score>=90:
    print("Grade: A — Excellent!")
elif score>=80 and score<=89:
    print("Grade: B — Very Good!")
elif score>=70 and score<=79:
    print("Grade: C — Good!")
elif score>=50 and score<=69:
    print("Grade: D — Pass")
else:
    print("Grade: F — Fail. Try harder!")

#Q5
weather = "raining"
have_umbrella = False
if weather=="raining":
    if have_umbrella==True:
        print("It's raining but you have an umbrella, you're good to go!")
    else:
        print("It's raining and you have no umbrella, stay home!")
elif weather=="sunny":
    print("Perfect weather, enjoy your day!")
else:
    print("Unknown weather, be careful!")

#Q6
score = 73
if score>=50:
    print("Pass")
else:
    print("Fail")
print ("Pass" if score>=50 else "Fail")

#Q7
allowed_users = ["Alice", "Bob", "Charlie", "Diana"]
blocked_ids = {101, 205, 399}
user_profile = {"username": "Alice", "role": "admin"}
if "Alice" in allowed_users:
    print("Welcome Mrs.Alice")
if "Eve" not in allowed_users:
    print("Sorry Mrs. Eve (accecss denied)")
if 205 in blocked_ids:
    print("Sorry your id isn't approved")
if "role" in user_profile:
    print(user_profile["role"])

#Q8
i=1
while i<=10:
    print(i)
    i+=1
else:
    print("Loop complete!")
j=0
while j<10:
    j+=1
    if j==5:
        continue
    print(j)
k=0
while k<10:
    k+=1
    print(k)
    if k==7:
        break

#Q9
grocery_list=[]
max_items=4
counter=1
while counter<=4:
    item=input(f"Please enter your {counter} item ")
    grocery_list.append(item.title().strip())
    counter+=1
else:
    print("List is full!")
grocery_list.sort()
i=0
while i<=3:
    print(grocery_list[i])
    i+=1
  
#Q10
menu_items = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]
restaurant_name = "YUMMY"
for i in range(len(menu_items)):
    print(i+1,".",menu_items[i])
for x in restaurant_name:
    print(x)
for y in menu_items:
    if y=="Pasta":
        break
    print(y)
print("\n")
for k in menu_items:
    if k =="Burger":
        continue
    print(k)

#Q11
class_grades = {
    "Omar":  {"Math": 88, "English": 92, "Science": 75},
    "Layla": {"Math": 95, "English": 80, "Science": 90},
    "Yusuf": {"Math": 100, "English": 98.5, "Science": 95}
}
for name in class_grades:
    print(name,":")
    for subject in class_grades[name]:
        score=class_grades[name][subject]
        print(f"score in {subject}={score}")

#Q12
account_balance = 1000
pin = "1234"
allowed_operations = ["deposit", "withdraw", "balance"]
pin2=input("Please enter your PIN:").strip()
if pin==pin2:
    print("PIN Accepted! Welcome.")
    counter=1
    while counter<=3:
        operations=input("Please choose your operation (deposit / withdraw / balance):").strip().lower()
        if operations in allowed_operations:
            if operations==allowed_operations[2]:
                print(f"Your current balance is:{account_balance}$")
            elif operations==allowed_operations[0]:
                deposit=int(input("How much do you want to deposit?"))
                account_balance+=deposit
                print(f"Deposited! New balance: {account_balance}$")
            elif operations=="withdraw":
                cash=int(input("How much do you want to withdraw?"))
                if cash>account_balance:
                    print("Insufficient funds!")
                else:
                    account_balance-=cash
                    print(f"Withdrawn! New balance: {account_balance}$")
        else:
            print("Invalid operation!")
        counter+=1
    else:
        print(f"Session complete. Final balance: {account_balance}$")
else:
    print("Wrong PIN! Access Denied.")