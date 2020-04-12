select s.Name as 'NAME', s.CWID AS 'CWID', g.Course AS 'COURSE', g.Grade AS 'GRADE', i.Name AS 'INSTRUCTOR'
from students s, grades g, instructors i
where s.CWID = g.StudentCWID and i.CWID = g.InstructorCWID
order by s.Name