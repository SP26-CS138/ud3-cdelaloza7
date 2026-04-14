'''
DEVELOPER(S): Chloe De La Loza
COLLABORATORS: None
DATE: April 13, 2026
'''

"""
A digital addiction tracker that logs the users daily screen time and provides a summary. 

The user enters how many hours they spend on each app in a list, and then the program calculates their total screen time and gives a usage rating.
"""

##########################################
# IMPORTS:
# No imports needed
##########################################


##########################################
# FUNCTIONS:
##########################################

def display_apps(apps):
    """
    Prints all tracked apps with a numbered menu
    apps: list of app name strings
    """
    print("\n[ Apps to Track ]")
    for i, app in enumerate(apps, start=1):
        print(f" {i}. {app}")

def get_hours(apps):
    """
    Asks the user to enter hours spent on each app. Returns a list of floats representing hours per app. 
    apps: list of app name strings
    """
    hours = []
    print("\nEnter how many hours you spent on each app today.\n")
    for app in apps:
        while True:
            entry = input(f"Hours on {app}: ").strip()
            try:
                hours.append(float(entry))
                break
            except ValueError:
                print(" Please enter a valid number.")
    return hours

def display_summary(apps, hours):
    """
    Prints a formatted summary of screen time per app and a usage rating.
    apps: list of app name strings
    hours: list of float hours matching each app
    """
    total = sum(hours)
    print("\n[ Your Screen Time Summary ]")
    for i in range(len(apps)):
        print(f"  {apps[i]}: {hours[i]:.1f} hrs")
    print (f"\n Total screen time: {total:.1f} hours")

    if total < 2:
        rating = "Healthy"
    elif total < 5:
        rating = "Moderate"
    elif total < 8:
        rating = "High"
    else:
        rating = "Addictive"
    
    print (f"Usage rating: {rating}")


##########################################
# MAIN PROGRAM:
##########################################

#NOTE: a list is used here because the apps are an ordered sequence
# of items that we loop through one by one. There are no named keys
# needed to look anything up, so a dictionary is not necessary

apps = [
    "Instagram",
    "Tiktok",
    "Youtube",
    "Twitter/X",
    "Netflix",
    "Video Games"
]

name = input("Enter your name: ").strip()
print (f"\nWelcome, {name}. Let's check your digital habits.")

display_apps(apps)
hours = get_hours (apps)
display_summary(apps, hours)
