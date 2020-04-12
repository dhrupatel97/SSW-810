select Grade, count(*) as 'Most_Frequent_Grade_for_SSW_810'
from grades
where Course = 'SSW 810'
group by Grade limit 1