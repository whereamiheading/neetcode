# Write your MySQL query statement below
with c as (select 
student_id,
course_id,
grade,
rank() over (partition by student_id order by grade desc, course_id asc  ) as rnk
from enrollments)
select student_id,
course_id,
grade
from c where rnk = 1 order by student_id asc
