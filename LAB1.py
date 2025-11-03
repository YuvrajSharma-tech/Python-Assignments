# Name: Yuvraj Sharma
# Date:2 November 2025
# Project:Daily calorie tracker

print("Welcome to daily calorie tracker")
print("Track your meals and their calories")

meals = []
calories = []

num_meals = int(input("How many meals do you want to eat today?"))

for i in range(num_meals):
    meal_name = input(f"Enter meal {i+1}: ")
    calorie_amount = float(input("Enter calories: "))
    calories.append(calorie_amount)

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("Enter your daily calorie limit: "))

if total_calories > daily_limit:
    print("Warning:You have exceeded your daily calorie limit")
else:
    print("You are within your daily calorie limit")


if len(calories) > 0:
    average_calories = total_calories / len(calories)
else:
    average_calories = 0


print("==Summary==")
print(f"{'Meal Name':<15}{'Calories'}")
print("-" * 18)

for meal,cal in zip(meals,calories):
    print(f"{meal:<15}{cal}")

print("-" * 18)
print(f"{'Total':<30}{total_calories}")
print(f"{'Average':<30}{average_calories:.2f}")