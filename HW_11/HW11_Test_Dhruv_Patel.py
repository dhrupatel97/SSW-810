"""
    Testing the data repository
"""

import unittest
from HW11_Dhruv_Patel import Student, Instructor, Major, Repository

class TestRepository(unittest.TestCase):
    
    def test_student_repository(self) -> None:
        """testing student table"""

        expected  = [
            ['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 540', 'SSW 555'}, [], 3.38],
            ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], {'SSW 540', 'SSW 555'}, {'CS 546', 'CS 501'}, 4.0], 
            ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 546', 'CS 501'}, 4.0], 
            ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5], 
        ]
        
        stu_repo = Repository('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_11', False)

        calculated = list()
        for cwid, student in stu_repo._students.items():
            calculated.append(student.student_records())

        self.assertEqual(expected, calculated)

    def test_instructor_repository(self) -> None:
        """testing instructor pretty table"""

        expected = {
            ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
            ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
            ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 570', 1)
        }

        ins_repo = Repository('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_11', False)

        calculated = {tuple(i) for instructor in ins_repo._instructors.values() for i in instructor.instructor_records()}
        
        self.assertEqual(expected, calculated)

    def test_major_repository(self) -> None:
        """testing major pretty table"""

        expected = {
            'SFEN': ['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
            'CS': ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]
        }

        mj_repo = Repository('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_11', False)

        calculated = {maj: mj.major_records() for maj, mj in mj_repo._majors.items()}
        
        self.assertEqual(expected, calculated)
    
    def test_instructor_table_db(self) -> None:
        """testing student grade summary pretty table"""

        expected = [
            ('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
            ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
            ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
            ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
            ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
            ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
            ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
            ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
            ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')
        ]

        test = Repository('E:\\Stevens Institute of Technology\\2nd Sem\\SSW 810\\Assignments\\HW_11', False)

        calculated = list()

        for row in test.instructor_table_db('C:\\sqlite\\810_startup.db'):
            calculated.append(row)

        self.assertEqual(expected, calculated)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)