import os
import datetime
import predict as pd

def appendToAttendanceFile(student_attended):
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"attendance_{today_date}.txt"

    with open(filename, "a") as file:
        for student in student_attended:
            file.write(f"+ {student}\n")

def appendToFile():
    recorded_audios_path = set()
    student_attended = set()

    recorded_files = os.listdir("dataset/predict")

    for files in recorded_files:
        predicted_student = pd.predict("dataset/predict/" + files)
        if predicted_student != "No matching speaker.":
            student_attended.add(predicted_student)

    if student_attended:
        appendToAttendanceFile(student_attended)

    print("\n List of students who attended classes today:")
    print("____________________________________________")
    for std in student_attended:
        print(std)
    print("____________________________________________")

appendToFile()
