import pandas as pd

def load_data():
    instructors = pd.read_csv('instructors.csv')
    lessons = pd.read_csv('lessons.csv')
    return instructors, lessons

def schedule_lessons(instructors, lessons):
    # Example scheduling algorithm (simplified)
    schedule = []
    for _, lesson in lessons.iterrows():
        available_instructors = instructors[instructors['availability'] == lesson['time']]
        if not available_instructors.empty:
            assigned_instructor = available_instructors.iloc[0]
            schedule.append((lesson['student'], assigned_instructor['name'], lesson['time']))
            instructors = instructors[instructors['name'] != assigned_instructor['name']]
    return schedule

def main():
    instructors, lessons = load_data()
    schedule = schedule_lessons(instructors, lessons)
    for student, instructor, time in schedule:
        print(f"Lesson for {student} with {instructor} at {time}")

if __name__ == "__main__":
    main()