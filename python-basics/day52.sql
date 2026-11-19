insert into student(name,birth_date,school_no,native_place,identity_card) values
('李明','2008-05-20','0002','汕头','445221200805201234'),
('王芳','2007-11-03','0003','梅州','445221200711032234'),
('陈强','2008-02-14','0004','汕头','445221200802141764');
update student set native_place='广州' where name='李明';
delete from student where name='陈强';
SELECT * FROM student;


