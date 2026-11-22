select name,Population from city order by Population desc limit 10;
select name,Population from city where countrycode='chn' order by Population limit 5;
select name,Continent,population from country order by Continent,Population desc;
select name,Population from city order by Population desc limit 20,10;
select continent,count(name) from country group by Continent order by count(name) desc;
select countrycode,count(name) from city group by countrycode having count(name)>=100 order by count(name) desc limit 3;