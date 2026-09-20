# PART 1 - user input
city = input("Enter your city name: ")
temp = float(input("Enter today's temperature in C:"))


# PART 2 - if statement
if temp > 35:
    print("warning it is very hot today")


# PART 3 - if -else
if temp > 25:
    print("Great day to go outside today!")
else:
    print("Grab a jacket before you go")

# PART 4 - if-elif-else
if temp > 35:
    print("Weather: Socorching hot")
elif temp > 25:
      print("Weather: warm and sunny")
elif temp > 15:
      print("weather: cool and breezy")
else:
    print("weather: cold-stay warm")

# PART 5 - datetime module
import datetime
import calendar

now = datetime.datetime.now()
print("city:", city)
print("Time now:", now)

print(calendar.calendar(now.year))