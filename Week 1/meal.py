'''
Problem: Implement a program that prompts the user for a time and outputs whether it’s breakfast time,
         lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all
'''

def main():
    time = input("Time:")
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
         print("Breakfast time")

    elif 12 <= converted_time <= 13:
         print("Lunch time")

    elif 18 <= converted_time <= 19:
         print("Dinner time")


def convert(time):
    hours,minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes/60


if __name__ == "__main__":
    main()

