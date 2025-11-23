print("Welcome to my Python program!")
#used print statement to introduce program
hours = input("How many hours did you study today? ")
#used input statement to allow users to get personalized results
hours = float(hours)
#converted the hours variable from input to float so that it can be used for calculations
weekly_hours = hours * 7
#used multiplication to estimate the amount of hours user will study in week based off one day
print(f"You are on track to study {weekly_hours} hours this week.")
#used f-string to properly format the results of the equation
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
#used a try-except as a simple way to handle errors