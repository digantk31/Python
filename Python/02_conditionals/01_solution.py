# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# age = 65
age_value = input("enter your age: ")
age = int(age_value)

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")