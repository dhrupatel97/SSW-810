from datetime import datetime, timedelta
from typing import Tuple, Dict, Iterator
from prettytable import PrettyTable
import os

# PART 1

def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """different cases for using datetime module"""
    
    dt1: str = "Feb 27, 2020"
    dt2: str = "Feb 27, 2019"
    dt3: str = "Feb 1, 2019"
    dt4: str = "Sep 30, 2019"
    
    datetime1: datetime = datetime.strptime(dt1, "%b %d, %Y")
    datetime2: datetime = datetime.strptime(dt2, "%b %d, %Y")
    datetime3: datetime = datetime.strptime(dt3, "%b %d, %Y")
    datetime4: datetime = datetime.strptime(dt4, "%b %d, %Y")

    f1: datetime = datetime1 + timedelta(days = 3)
    f2: datetime = datetime2 + timedelta(days = 3)
    f3: int = datetime4 - datetime3

    three_days_after_02272020: str = f1.strftime("%b %d, %Y")
    three_days_after_02272019: str = f2.strftime("%b %d, %Y")
    days_passed_02012019_09302019: int = f3.days
    

    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019


# PART 2

def file_reader(path, num_fields, sep, header=False) -> Iterator[Tuple[str]]:
    """ function to return the tuple separated with separator , if any value error comes it should display the error on the line and expected value"""
    try:
        fp = open(path , 'r')
    except FileNotFoundError:
        raise FileNotFoundError("path not found")
    else:
        with fp:
            for n , line in enumerate(fp , 1):
                fields = line.rstrip('\n').split(sep)
                if len(fields) != num_fields:
                    raise ValueError(f"'{path}' line:{n} read {len(fields)} but expected {num_fields}")
                elif n > 1 or header is False:
                    yield tuple(fields)

# PART 3 
class FileAnalyzer():

    def __init__(self, directory):
        """define directory"""

        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()

        self.analyze_files()

    def analyze_files(self):
        """ define analyze files """

        path: str = self.directory
        try:
            dr: str = os.listdir(path)
        except FileNotFoundError:
            raise FileNotFoundError('No such directory')
        else:
            for file in dr:
                if file.endswith('.py'):
                    try:
                        fp = open(os.path.join(path, file), 'r')
                    except FileNotFoundError:
                        raise FileNotFoundError('No such File Found')
                    else:
                        with fp:
                            char_count: int = 0
                            class_count: int = 0
                            func_count: int = 0
                            line_count: int = 0

                            for line in fp:
                                char_count += len(line)
                                line_count += 1

                                if line.startswith('class '):
                                    class_count += 1

                                if line.strip().startswith('def '):
                                    func_count += 1

                            self.files_summary[file] = {
                                'classes': class_count,
                                'functions': func_count,
                                'lines': line_count,
                                'characters': char_count
                            }

    def pretty_print(self):
        """ Return the table """

        x = PrettyTable()
        x.field_names = ['File Name', 'Classes', 'Functions', 'Lines', 'Characters']

        for i, j in self.files_summary.items():
            x.add_row([i, j['classes'], j['functions'], j['lines'], j['characters']])

        return x

