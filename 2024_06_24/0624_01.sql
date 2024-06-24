CREATE TABLE IF NOT EXISTS student (
	student_id Serial Primary key,
   name varchar(20) NOT NULL,
   major varchar(20)
);

drop table youbike;

CREATE TABLE IF NOT EXISTS youbike (
	_id Serial Primary key,
    sna varchar(50) NOT NULL,
    sarea varchar(50),
    ar varchar(100),
	mday timestamp,
	updateTime timestamp,
	total smallint,
	rent_bikes smallint,
	retuen_bikes smallint,
	lat real,
	lng real
);
