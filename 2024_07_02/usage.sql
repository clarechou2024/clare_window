select count(*) as 數量
from youbike

select *
from youbike

CREATE TABLE IF NOT EXISTS youbike(
                _id Serial Primary Key,
                sna VARCHAR(50) NOT NULL,
                sarea VARCHAR(50),
                ar VARCHAR(100),
                mday timestamp,
                updateTime timestamp,
                total SMALLINT,
                rent_bikes SMALLINT,
                return_bikes SMALLINT,
                lat REAL,
                lng REAL,
                act boolean,
				UNIQUE (sna, updatetime));

INSERT INTO youbike(sna, sarea, ar, mday, updatetime, total, rent_bikes,return_bikes,lat,lng,act)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
			ON CONFLICT (sna, updateTime)
			DO NOTHING;