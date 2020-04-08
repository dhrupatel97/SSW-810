"""
    Testing the data repository
"""

import unittest
from HW10_Dhruv_Patel import Student, Instructor, Major, Repository

class TestRepository(unittest.TestCase):
    
    def test_student_repository(self) -> None:
        """testing student table"""

        expected  = [
            ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, [], 3.44],
            ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, [], 3.81], 
            ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 540', 'SSW 564'}, {'CS 501', 'CS 513', 'CS 545'}, 3.88], 
            ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, {'CS 501', 'CS 513', 'CS 545'}, 3.58], 
            ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'},{'CS 501', 'CS 513', 'CS 545'}, 4.0], 
            ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], {'SYS 612', 'SYS 671', 'SYS 800'}, [], 3.0], 
            ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 612', 'SYS 671'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 3.92],
            ['11658', 'Kelly, P', 'SYEN', [], {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 0], 
            ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 3.0], 
            ['11788', 'Fuller, E', 'SYEN', ['SSW 540'],{'SYS 612', 'SYS 671', 'SYS 800'}, [], 4.0]]
        
        stu_repo = Repository('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_10', False)

        calculated = list()
        for cwid, student in stu_repo._students.items():
            calculated.append(student.student_records())

        self.assertEqual(expected, calculated)

    def test_instructor_repository(self) -> None:
        """testing instructor pretty table"""

        expected = {
            ('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
            ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
            ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
            ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
            ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
            ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
            ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
            ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)
        }

        ins_repo = Repository('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_10', False)

        calculated = {tuple(i) for instructor in ins_repo._instructors.values() for i in instructor.instructor_records()}
        
        self.assertEqual(expected, calculated)

    def test_major_repository(self) -> None:
        """testing major pretty table"""

        expected = {
            'SFEN': ['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'] ,['CS 501', 'CS 513', 'CS 545']],
            'SYEN': ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]
        }

        mj_repo = Repository('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_10', False)

        calculated = {maj: mj.major_records() for maj, mj in mj_repo._majors.items()}
        
        self.assertEqual(expected, calculated)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)