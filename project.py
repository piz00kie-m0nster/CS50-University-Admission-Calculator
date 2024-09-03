
# defines main function
def main():
    print("Welcome to the CS50 University Admission Calculcator!")
    print("We hope you gain more insight into your chances of gaining admission at CS50 University.")
    print()
    print("Option 1: Engineering\nOption 2: Medicine\nOption 3: Business\nOption 4: Art\n")
    while True:
        major = input("The first step is to pick your major. Choose from one of the 4 options above: ")
        major_chance = pick_major(major)
        if major_chance == "Not valid":
            pass
        else:
            break
    print()
    while True:
        grades_list = input("Great choice of major! Now, enter a list of your most recent semester grades for each of your 7 classes(separated by commas):\n")
        grade_chance = enter_grades(grades_list)
        if grade_chance == "Not valid":
            pass
        else:
            break
    print()
    print("Now please enter the number of activities you participate in (max of 10), how many hours you complete each week, and the number of weeks per year:")
    while True:
        try:
            num_activities = int(input("Activities: "))
            if num_activities > 10 or num_activities < 0:
                pass
            else:
                break
        except:
            pass
    while True:
        try:
            hours = int(input("Hours: "))
            if hours > 168 or hours < 0:
                pass
            else:
                break
        except:
            pass
    while True:
        try:
            weeks = int(input("Weeks: "))
            if weeks > 52 or weeks < 0:
                pass
            else:
                break
        except:
            pass
    while True:
        activity_chance = activities(num_activities, hours, weeks)
        if activity_chance == "Not valid":
            pass
        else:
            break
    print()
    while True:
        try:
            num_awards = int(input("Please enter how many awards you have recieved, up to 10 awards: "))
            awards_chance = awards(num_awards)
            if awards_chance == "Not valid":
                pass
            else:
                break
        except:
            pass
    print()
    while True:
        essay_quality = input("Please enter the quality of your written essays as a percentage: ")
        essay_chance = supp_essays(essay_quality)
        if essay_chance == "Not valid":
            pass
        else:
            break
    print()
    print("Just a bit more to go. Enter how many recommendation letters you are submitting, up to 3, and how well your teachers know you as a percentage. ")
    while True:
        try:
            num_letters = int(input("Number of recommendation letters: "))
            if num_letters > 3 or num_letters < 0:
                pass
            else:
                break
        except:
            pass
    while True:
        rec_quality = input("How well your teachers know you: ")
        rec_chance = rec_letters(num_letters, rec_quality)
        if rec_chance == "Not valid":
            pass
        else:
            break
    print()
    print("Option 1: Early Decision\nOption 2: Regular Decision\n")
    while True:
        decisions = input("Ok, just one last step. Please enter under which cycle you are going to submit your application from the options above: ")
        decision_chance = decision_time(decisions)
        if decision_chance == "Not valid":
            pass
        else:
            break
    print()
    final_chance = calculate_chance(major_chance, grade_chance, activity_chance, awards_chance, essay_chance, rec_chance, decision_chance)
    print(f"Thank you for taking the time to try out the CS50 University Admission Calculator. You have a {round(final_chance, 2)}% chance of being accepted into CS50 University.")


# returns chance of acceptance based on the chosen major
def pick_major(major):
    major = major.replace(" ", "")
    major = major.casefold()
    if major in ["engineering", "medicine", "business", "art"]:
        if major == "engineering":
            return 25
        elif major == "medicine":
            return 45
        elif major == "business":
            return 60
        elif major == "art":
            return 75
    else:
        return "Not valid"

# returns chance of acceptance based on the grades inputed
def enter_grades(grades):
    grades_list = grades.split(", ")
    chance = 0
    if len(grades_list) != 7:
        return "Not valid"
    else:
        for grade in grades_list:
            try:
                if int(grade) > 100 or int(grade) < 0:
                    return "Not valid"
                elif int(grade) > 90:
                    chance += 14
                elif int(grade) > 75:
                    chance += 9
                elif int(grade) > 50:
                    chance += 3
                elif int(grade) > 0:
                    chance += 0
            except:
                return "Not valid"
        return chance

# returns chance of acceptance based on the number of activities
# the student does and how many hours per week per year
def activities(num_activities, hours, weeks):
    if int(num_activities) > 10 or int(hours) > 168 or int(weeks) > 52:
        return "Not valid"
    if int(num_activities) < 0 or int(hours) < 0 or int(weeks) < 0:
        return "Not valid"
    amount = int(num_activities) * int(hours) * int(weeks)
    if not amount > 0:
        return "Not valid"
    else:
        if amount > 6000:
            return 85
        elif amount > 4500:
            return 75
        elif amount > 2500:
            return 60
        elif amount > 1000:
            return 45
        elif amount > 500:
            return 30
        elif amount > 250:
            return 20
        elif amount > 100:
            return 15
        elif amount > 50:
            return 5
        else:
            return 0

# returns chance of acceptance based on the number of awards
def awards(num_awards):
    AWARD_MULTIPLIER = 10
    if int(num_awards) > 10 or int(num_awards) < 0:
        return "Not valid"
    else:
        chance = num_awards * AWARD_MULTIPLIER
    return chance

# returns chance of acceptance based on the quality of
# the supplemental essays
def supp_essays(quality):
    if not quality.endswith("%"):
        return "Not valid"
    quality = quality.replace("%", "")
    try:
        quality = int(quality)
        if quality > 100 or quality < 0:
            return "Not valid"
        else:
            return quality
    except:
        return "Not valid"


# returns chance of acceptance based on the number of recommendation
# letters and how well they are written
def rec_letters(num_letters, quality):
    if not quality.endswith("%"):
        return "Not valid"
    try:
        if int(num_letters) > 3 or int(num_letters) < 0:
            return "Not valid"
        else:
            try:
                amount = int(num_letters) * int(quality.replace("%", ""))
                if int(quality.replace("%", "")) > 100 or int(quality.replace("%", "")) < 0:
                    return "Not valid"
                if amount > 250:
                    return 100
                elif amount > 125:
                    return 75
                elif amount > 75:
                    return 50
                elif amount > 40:
                    return 35
                else:
                    return 0
            except:
                return "Not valid"
    except:
        return "Not valid"

# returns chance of acceptance based on whether the student
# submits the essays early decision regular decision
def decision_time(time):
    time = time.casefold()
    if time in ["regular decision", "early decision", "rd", "ed"]:
        if time == "regular decision" or time == "rd":
            return 75
        else:
            return 85
    else:
        return "Not valid"


# calculates and returns the chance of acceptance using
# the given information from the student using a special formula
def calculate_chance(major, grades, activities, awards, essays, recommendation, decision):
    MAJOR_MULTIPLIER = 0.2
    GRADE_MULTIPLIER = 0.35
    ACTIVITY_MULTIPLIER = 0.25
    AWARD_MULTIPLIER = 0.075
    ESSAY_MULTIPLIER = 0.075
    REC_MULTIPLIER = 0.025
    DECISION_MULTIPLIER = 0.025
    major_chance = int(major) * MAJOR_MULTIPLIER
    grade_chance = int(grades) * GRADE_MULTIPLIER
    activity_chance = int(activities) * ACTIVITY_MULTIPLIER
    award_chance = int(awards) * AWARD_MULTIPLIER
    essay_chance = int(essays) * ESSAY_MULTIPLIER
    rec_chance = int(recommendation) * REC_MULTIPLIER
    decision_chance = int(decision) * DECISION_MULTIPLIER
    final_chance = major_chance + grade_chance + activity_chance + award_chance + essay_chance + rec_chance + decision_chance
    return final_chance



# executes main function
if __name__ == "__main__":
    main()
