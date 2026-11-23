# insert into 表(列) values (值),(值);
# update 表 set 列=值 where 条件;
# delete from 表 where 条件;
# select 列 from 表 where 条件 group by 列 having 条件 order by 列 desc limit 跳过,条数;
create table school.course(
id int primary key auto_increment,
name varchar(30) not null,
teacher varchar(20),
credit int
);
alter table school.course add classroom varchar(20);
alter table school.course modify teacher varchar(30);
insert into school.course(name,teacher,credit) values
('数学','jack',5),
('语文','tom',8),
('英语','mike',9);
update school.course set teacher='taylor' where name='数学';
delete from school.course where name='数学';
SELECT * from school.course;
select name,population from world.city where countrycode = 'CHN';
select name,population from world.city where Population between 1000000 and 2000000;
select name from world.country where name like 'a%';
select count(name) from world.country where indepyear is null;
select continent,avg(LifeExpectancy) from world.country group by continent;
select countrycode,count(name) from world.city group by countrycode having count(name)>=100;
select name,population from world.city order by Population desc limit 10;
select name,population from world.city order by Population desc limit 20,20;
select count(name) from world.country group by continent order by count(name) desc;



