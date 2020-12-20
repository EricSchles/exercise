import pandas as pd
from datetime import datetime

log = pd.read_csv("exercise_log.csv")

tmp = {}
tmp["number_of_hours_slept_previous_night"] = float(input("How many hours did you sleep last night? (enter a number)"))
print()
tmp["exercise"] = str(input("What exercise did you do? (yoga, core, legs, arms, all, bike, rowing, run, rock climbing)"))
print()
tmp["number_of_meals_prior_to_workout"] = float(input("How many meals did you eat before the workout? (enter a number)"))
print()
tmp["calories_eaten_prior_to_workout_that_day"] = float(input("How many calories did you eat prior to workout that day? (enter a number)"))
print()
tmp["sweat_during_workout"] = int(input("Did you sweat during the workout? (enter 1 for yes, 0 for no)"))
print()
tmp["workout_duration"] = float(input("How long did you workout for? (enter a number)"))
print()
tmp["highest_workout_intensity"] = str(input("What was the most intense the workout got? (low, medium, high)"))
print()
tmp["is_warmup"] = int(input("Was this a warmup workout? (enter 1 for yes, 0 for no)"))
print()
tmp["time_of_start_of_workout"] = datetime.strptime(str(input("When did you start the workout? (enter year, month, day, hour, minute)")), '%Y %m %d %H %M')
print()
tmp["time_of_end_of_workout"] = datetime.strptime(str(input("When did you end the workout? (enter year, month, day, hour, minute)")), '%Y %m %d %H %M')
print()
tmp["number_of_breaks_taken_during_workout"] = int(input("How many breaks did you take during the workout? (enter a number)"))
print()
tmp["weight_directly_prior_to_workout"] = float(input("How much did you weigh before the workout? (enter a number)"))
print()
tmp["weight_directly_after_workout"] = float(input("How much did you weigh after the workout? (enter a number)"))
print()
tmp["water_drank_during_workout"] = int(input("Did you drink water during the workout? (enter 1 for yes, 0 for no)"))
print()
tmp["body_part_focus_of_workout"] = str(input("What body part did you focus on during the workout? (all, legs, core, arms)"))
print()
tmp["level_of_fatigue_going_into_workout"] = str(input("How fatigued were you going into the workout? (low, medium, high)"))
print()
tmp["stress_level_going_into_workout"] = str(input("How stressed were you going into the workout? (low, medium, high)"))
print()
tmp["number_of_days_since_last_workout"] = int(input("How many days since your last workout? (enter a number)"))
print()
tmp["temperature_outside_during_workout"] = int(input("What was the temperature in fahrenhiet? (enter a number)"))
log = log.append(tmp, ignore_index=True)

log.to_csv("exercise_log.csv", index=False)






