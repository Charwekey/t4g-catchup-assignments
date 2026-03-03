

firstname = 'Charwekey'
lastname = 'Sabutey'
full_name = (f"{firstname} {lastname}")
age = 20
current_week = 4
cohort = 4
fav_topic = 'loops'
cohort_class = 'Backend Class'
skills_good = "Frontend development"



cohort_updated= cohort_class.upper()
fullname= full_name.title()
fav_topic_updated = fav_topic.replace("loops", "functions")


print(f" {'PROFILE CARD':^38}")  
print(f"Name: {fullname} ")
print(f"Age: {age}")
print(f"Class: {cohort_updated}")
print(f"Cohort: {cohort} (Week {current_week})")
print(f"Favourite Topic: {fav_topic_updated} ")
print(f"Skills I’m Good At: {skills_good}\n")


current_week = 4
weeks_left = 12 - current_week
print(f"Weeks left in the program: {weeks_left:<18} ")