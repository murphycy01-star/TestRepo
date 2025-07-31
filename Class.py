# Define two sets of student names who passed Math and English
passed_math = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
passed_english = {"Charlie", "Eve", "Frank", "Grace", "Bob"}

# 1. Students who passed both subjects
both_subjects = passed_math & passed_english
print(" Passed both Math and English:", both_subjects)

# 2. Students who passed only Math
only_math = passed_math - passed_english
print(" Passed only Math:", only_math)

# 3. Students who passed only English
only_english = passed_english - passed_math
print(" Passed only English:", only_english)

# 4. All students who passed at least one subject
passed_any = passed_math | passed_english
print(" Passed at least one subject:", passed_any)

# 5. Add a new student to Math pass list
passed_math.add("Helen")
print(" After adding Helen to Math:", passed_math)

# 6. Remove a student who was added by mistake
passed_math.discard("Diana")  # discard won't throw error if not found
print(" After removing Diana from Math:", passed_math)

# 7. Check if a particular student passed English
print(" Did Frank pass English?", "Frank" in passed_english)

# 8. Clear all students from English set
# passed_english.clear()
# print("🧹 After clearing English set:", passed_english)

# 9. Convert to list and sort
sorted_all = sorted(list(passed_any))
print("Sorted list of students who passed at least one subject:", sorted_all)
