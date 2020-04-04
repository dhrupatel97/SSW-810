import unittest
from HW08_Dhruv_Patel import date_arithmetic, file_reader, FileAnalyzer


class TestDateArithemitic(unittest.TestCase):

    def test_date_arithmetic(self):
        """ Test case to check date arithmetic operations """

        self.assertEqual(date_arithmetic(), ('Mar 01, 2020', 'Mar 02, 2019', 241))

class TestFileReader(unittest.TestCase):

    def test_file_reader(self):
        """ Test case to extract file content """

        a = list()
        b = ["('123', 'Jin He', 'Computer Science')", "('234', 'Nanda Koka', 'Software Engineering')","('345', 'Benji Cai', 'Software Engineering')"]

        for items in file_reader('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_08/students_major.txt', 3, sep='|', header=True):
            a.append(f"{items}")

        self.assertEqual(a, b)

class TestFileAnalyzer(unittest.TestCase):

    def test_file_analyzer(self):
        """Test Case for scanning files"""

        fa = FileAnalyzer('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_08')

        expected = {
            '0_defs_in_this_file.py': {
                'classes': 0,
                'functions': 0,
                'lines': 3,
                'characters': 57
            },
            'file1.py': {
                'classes': 2,
                'functions': 4,
                'lines': 25,
                'characters': 270
            },
            'HW08_Dhruv_Patel.py': {
                'classes': 1,
                'functions': 5,
                'lines': 120,
                'characters': 3834
            },
            'HW08_Test_Dhruv_Patel.py': {
                'classes': 3,
                'functions': 3,
                'lines': 63,
                'characters': 1917
            }
        }

        self.assertEqual(expected, fa.files_summary)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
