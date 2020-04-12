select Name, cwid, count(Course) as 'Total_Course_Taken'
from students join grades
on students.CWID = grades.StudentCWID
group by Name, cwid