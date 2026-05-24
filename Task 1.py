#Q1
name="Youssef"
age=16
GPA=4.0
student=True
print(f"My name is {name},I am {age} years old,My GPA={GPA},Am I a student={student}")
print(type(name),type(age),type(GPA),type(student))

#Q2
city,country,population="New York","USA","342.5m"
print(f"The city is {city},The Country is {country},The population of the country={population}")

#Q3
score=95.8
print(int(score))
#I got 95 because int function converted the type from float to int and int doesn't have decimal so the number was floored to 95

#Q4
items=250
customers=7
bought_items=3
left_items=items-(customers*bought_items)
print(f"The left items={left_items}")
print(f"Each customer paid {bought_items*15.5}EGP")
print("The remainder when the leftover items are packed in boxes of8=",left_items%8)

#Q5
Square_sideLength=6
Rectangle_length,Rectangle_width=9,4
print(f"A of square={Square_sideLength**2} , A of rectangle={Rectangle_length*Rectangle_width}")

#Q6
x,y=17,5
print(x/y)
#It will give decimal(float) value because it is normal divison
print(x//y)
#It will give an integer number because // floors the number and it won't give 3.0 it will give 3 because x,y are integers
print(x%y)
#It will give the reminder of the divison

#Q7
name="Youssef Mohamed"
print(f"My first name is {name[0:7]} , My last name is {name[8:15]} , The last 3 characters of my full name={name[12:15]}")

#Q8
sentence="Python is fun to learn"
print(f"The length of the sentence={len(sentence)},The full sentence:{sentence[:]},character with index 7:{sentence[7]},from character with index10:{sentence[10:]}")

#Final Question
full_name="Youssef Mohamed"
age=16
gpa=3.8
is_student=True
city,country="15 may city","Egypt"
Math,Science,English=100.0,95.3,98.5
total=Math+Science+English
Avg=total/3
print(f"The total={total} , The Avg={Avg} , The Avg in int={int(Avg)}")
print(f"The first name is {full_name[0:7]} , The first letter={full_name[0]} , The length of the full name={len(full_name)}")
print(f"My name is {full_name} and I am {age} years old, I live in {city}, {country}, Am I student={is_student}, My GPA={gpa} and my total score={total}")