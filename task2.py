#Q1
heroes=["Spider-man","Batman","Ironman","Deadpool"]
heroes.append("Superman")
heroes.insert(1,"Wolverine")
popped_hero=heroes.pop(5)
heroes.sort()
print(heroes)
print(popped_hero)

#Q2
coordinates=(0,3,22)
x,y,z=coordinates
print(f"x={x},y={y},z={z}")
#if i wrote coordinates[0]=10 it will result an error because the Tuples( ) cannot be edited

#Q3
backend_skills = {"Python", "Java", "C++", "SQL"}
frontend_skills = {"HTML", "CSS", "JavaScript", "Python"}
print(backend_skills.intersection(frontend_skills))
print(backend_skills.difference(frontend_skills))
print(backend_skills.symmetric_difference(frontend_skills))

#Q4
employee={
    "Name":"Ahmed",
    "Age":22,
    "skills":["ML","NLP","Automation"]
}
employee.update({"department":"IT"})
employee.update({"Age":23})
print(employee["skills"][1])
print(employee)

#Q5
user_cart={
    "username":"Youssef",
    "items":[("Laptop", 50000),("Mouse", 2000)],
    "unique_categories":{"Electronics", "Accessories"}
}
user_cart["items"].append(("Monitor",12000))
user_cart["unique_categories"].add("PC Hardware")
item_name,item_price=user_cart["items"][0]
no_unique=len(user_cart["unique_categories"])
print(f"Username:{user_cart['username']},The name of the bought item:{item_name} and its price={item_price},The total number of unique categories:{no_unique}")