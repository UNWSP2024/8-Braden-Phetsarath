#Braden Phetsarath
# 10/20

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.
def course_info():
    courses = {}

    while True:
        course_id = input("Enter course ID (or type 'done' to finish)(ex. COS 2005): ").strip()
        if course_id.lower() == "done":
            break
        course_name = input(f"Enter course name for {course_id}: ").strip()
        courses[course_id] = course_name

    return courses
def course_question():
    subject = input("Enter the course subject (ex. COS):")
    return subject

def main():
    courses = course_info()
    subject = course_question().upper()

    print(f"\n Courses under the subject {subject}")
    found = False
    for course_id, course_name in courses.items():
        if course_id.upper().startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True
    if not found:
        print("No such course under that subject.")
if __name__ == "__main__":
    main()
