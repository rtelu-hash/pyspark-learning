#Homework before lesson 2 
#Write a small script that:
#Creates a list of 5 employees — each employee is a dictionary with name, salary, department
#Loops through the list
#Uses your check_price logic — but for salary — print "High earner" if salary > 50000, else "Low earner"

# Define the employee dictionary
employee = [
    {"name": "Ravi", "salary": 1000000, "Department": "AIA"},
    {"name": "Hanu", "salary": 3000000, "Department": "MUSICAL AI"},
    {"name": "Aaru", "salary": 400000, "Department": "CLOUD SOLUTIONS AI"},
    {"name": "Sukku", "salary": 500000, "Department": "DANCE AI"},
    {"name": "Ivaan", "salary": 700000, "Department": "NEW BORN AI"}
]

#Define the check_sal function

def check_sal(salary):
    if salary > 500000:
        return "High earner"
    else:
        return "Low earner"
#Run the loop to check the dalary and print if high earner or low earner

for emp in employee:
    print(emp["name"],"-", emp["salary"], check_sal(emp["salary"]))
        


    