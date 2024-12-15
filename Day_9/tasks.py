# # Add to dictionary
# dictionary_name[key] = value
# # Wiping a dictionary or creating a new one
# dictionary_name = {}
# # retrieving from a dictionary
# dictionary_name['key']
# # editing a dictionary
# dictionary_name['key_to_edit'] = 'new_value'

# # Automatic Grading Program
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for name in student_scores:
#     grades = student_scores[name]
    
#     if 91 <= grades <= 100:
#         student_grades[name] = "Outstanding"
#     elif 81 <= grades <= 90:
#         student_grades[name] = "Exceeds Expectations"
#     elif 71 <= grades <= 80:
#         student_grades[name] = "Acceptable"
#     else:
#         student_grades[name] = "Fail"
# print(student_grades)