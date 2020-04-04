def file_reading(path: str, fields: int, sep: str = ',', header=False):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist')
    else:
        with fp:
            count = 0
            # reader = csv.reader(fp, delimiter=sep)

            for line in fp:
                count += 1
                line = line.strip('\n')
                line = line.split(sep)
                # p = len(line)
                # print(p)
                if len(line) != fields:
                    raise ValueError(f'{path} has {len(line)} fields on line {count} but expected {fields}')

                if header == False:
                    yield tuple(line)
                else:
                    header = False

def runn():
    """ Test case to extract file content """

    a = list()
    b = ["('123', 'Jin He', 'Computer Science')", "('234', 'Nanda Koka', 'Software Engineering')","('345', 'Benji Cai', 'Software Engineering')"]

    for items in file_reading('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_08/students_major.txt', 3, sep='|', header=True):
        a.append(f"{items}")
    print(a)
    print(b)


# file_reading('E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_08/students_major.txt', 3, sep='|', header=True)
runn()