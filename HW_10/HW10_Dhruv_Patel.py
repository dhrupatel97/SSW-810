"""
    Creating a data repository for an university
    which can be used to track the student, courses, grades. 
    Also, can view details about the instructors and course taught.
    Additional functionality tracks the required courses and elective course remaining 
    based on the passing criteria

"""


from typing import Dict, Set, Tuple
from collections import defaultdict
import os
from HW08_Dhruv_Patel import file_reader
from prettytable import PrettyTable

class Student:
    """adding a single student"""

    def __init__(self, cwid: int, name: str, major: str) -> None:
        """creating an instance of student after reading each line in the file"""

        self._cwid: int = cwid
        self._name: str = name
        self._major: str = major
        self._course = dict()
    
    def add_course(self, course: str, grade: str) -> None:
        """adding grade to the course"""

        self._course[course]: Dict[str, str] = grade
    
    def student_records(self) -> list:
        """display the records"""
        
        major, passed, rem_r, rem_ele, GPA = self._major.remaining_course(self._cwid, self._course)
        
        return [self._cwid, self._name, major, sorted(passed), rem_r, rem_ele, GPA]

class Instructor:
    """adding about a single instructor"""

    def __init__(self, cwid: int, name: str, department: str) -> None:
        """creating new instance of instructor after reading the file"""

        self._cwid: int = cwid
        self._name: str = name
        self._department: str = department
        self._course_inst: Dict[str, int] = defaultdict(int)
    
    def add_student(self, course: str) -> None:
        """increamenting the count of student for the course taken under the instructor"""

        self._course_inst[course] += 1

    def instructor_records(self) -> list:
        """display records"""

        for course, count in self._course_inst.items():
            yield [self._cwid, self._name, self._department, course, count]

class Major:
    """adding major separately with the required and elective course"""

    def __init__(self, major: str) -> None:
        """creating new instance"""

        self._major: str = major
        self._required = dict()
        self._electives = dict()

    def add_course(self, course: str, flag: str) -> None:
        """adding flag to the major when this function is called"""
        
        if flag == 'R':
            self._required[course] = flag
        elif flag == 'E':
            self._electives[course] = flag
        else:
            print(f"Unknown Flag found {flag}")
        
    def remaining_course(self, cwid, completed) -> tuple:
        """finding remaining courses"""
        
        passing_grades: Set[str] = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

        passed: Set[str] = {course for course, grade in completed.items() if grade in passing_grades}
        

        rem_r: Set[str] = set(self._required) - passed
        re: Set[str] = set(self._electives)

        if re.intersection(passed):
            rem_ele = []
        else:
            rem_ele = re
        
        
        gpa: float = 0.0
        GPA: float = 0.0
        
        grade_point: Dict[str, float] = {
            'A': 4.0,
            'A-': 3.75,
            'B+': 3.25,
            'B': 3.0,
            'B-': 2.75,
            'C+': 2.25,
            'C': 2.0,
            'C-': 0,
            'D+': 0,
            'D': 0,
            'D-': 0,
            'F': 0
        }

        for grade in completed.values():
            for g, p in grade_point.items():
                if grade == g:
                    gpa += p

        if len(passed) == 0:
            print(f"Student {cwid} has not passed with minimum grade point")
        else:
            GPA = round(gpa/len(passed), 2)

        return self._major, passed, rem_r, rem_ele, GPA

    def major_records(self) -> list:
        """display records"""

        return [self._major, sorted(self._required), sorted(self._electives)]

class Repository:

    def __init__(self, dir: str, to_run: bool = True) -> None:
        """initialize the files to read them one by one"""

        self._dir: str = dir
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._majors: Dict[str, Major] = dict()

        try:
            self._get_major(os.path.join(dir, 'majors.txt'))
            self._get_students(os.path.join(dir, 'students.txt'))
            self._get_instructors(os.path.join(dir, 'instructors.txt'))
            self._get_grades(os.path.join(dir, 'grades.txt'))
            
        except FileNotFoundError as x:
            print(x)
        else:
            if to_run:
                print('------STUDENT SUMMARY-----')
                self.student_table()
                print('------INSTRUCTOR SUMMARY-----')
                self.instructor_table()
                print('------MAJOR SUMMARY--------')
                self.major_table()
    
    def _get_students(self, path: str) -> None:
        """reading the file and adding student to the container"""

        for cwid, name, major in file_reader(path, 3, sep = ';', header = True):
            if major not in self._majors:
                print(f"Student {cwid} '{name}' has unknown major '{major}'")
            else:
                self._students[cwid] = Student(cwid, name, self._majors[major])
    
    def _get_instructors(self, path: str) -> None:
        """reading the file and adding instructor to the container"""

        for cwid, name, department in file_reader(path, 3, sep = '|', header = True):
            self._instructors[cwid] = Instructor(cwid, name, department)
    
    def _get_grades(self, path: str) -> None:
        """reading the file and adding grades to respective student"""

        for st_cwid, course, grade, in_cwid in file_reader(path, 4, sep = '|', header = True):
            if st_cwid in self._students:
                self._students[st_cwid].add_course(course, grade)
            else:
                print(f"Grade for unknown {st_cwid}")
            
            if in_cwid in self._instructors:
                self._instructors[in_cwid].add_student(course)
            else:
                print(f"Grade given by unknown {in_cwid}")
    
    def _get_major(self, path: str) -> None:
        """reading major file"""

        for major, flag, course in file_reader(path, 3, sep = '\t', header = True):
            if major not in self._majors:
                self._majors[major] = Major(major)
            self._majors[major].add_course(course, flag)
            
    def student_table(self) -> None:
        ptable = PrettyTable(field_names=['CWID', 'NAME', 'MAJOR', 'COMPLETED COURSES', 'REMAINING REQUIRED', 'REMAINING ELECTIVES', 'GPA'])

        for student in self._students.values():
            ptable.add_row(student.student_records())

        print(ptable)

    def instructor_table(self) -> None:
        ptable = PrettyTable(field_names=['CWID', 'NAME', 'DEPARTMENT', 'COURSE', 'COUNT'])

        for instructor in self._instructors.values():
            for i in instructor.instructor_records():
                ptable.add_row(i)

        print(ptable)
    
    def major_table(self) -> None:
        ptable = PrettyTable(field_names=['MAJOR', 'REQUIRED COURSES', 'ELECTIVE COURSES'])

        for major in self._majors.values():
            ptable.add_row(major.major_records())
        
        print(ptable)


def main():
    
    Repository('E:\\Stevens Institute of Technology\\2nd Sem\\SSW 810\\Student-Repository')


if __name__ == '__main__':
    main()