from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/students')
def completed_courses() -> str:
    """find the student grade summary through db"""

    db: sqlite3.Connection = sqlite3.connect('C:\\sqlite\\810_startup.db')

    query: str = "select s.Name, s.CWID, g.Course, g.Grade, i.Name from students s, grades g, instructors i where s.CWID = g.StudentCWID and i.CWID = g.InstructorCWID order by s.Name"

    my_data = [{'student': student, 'cwid': cwid, 'course': course, 'grade': grade, 'instructor': instructor} for student, cwid, course, grade, instructor in db.execute(query)]

    db.close()

    return render_template('student_main.html',
    title = 'Student Repository',
    header = 'Student Repository',
    sub_header = 'Student, Course, Grade, Instructor',
    student = my_data)

if __name__ == '__main__':
   app.run()