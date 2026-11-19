use school;
create table course(
	id int primary key auto_increment,
	course_name varchar(20),
	credit float,
	period int,
	start_date date,
	createtime timestamp
);
DESC course;
ALTER TABLE course ADD teacher VARCHAR(20);

DESC course;

DROP TABLE course;

DESC course;

SHOW TABLES;