CREATE TABLE 使用者(
	user_id SERIAL PRIMARY KEY,
	姓名 VARCHAR(20),
	性別 VARCHAR(20),
	連絡電話 VARCHAR(20),
	電子郵件 VARCHAR(40),
	isGetEmail Bool,
	出生年月日 VARCHAR(20),
	自我介紹 VARCHAR(200),
	密碼 VARCHAR(100),
	連線密碼 VARCHAR(100)
);

INSERT INTO 使用者
	("姓名", "性別", "聯絡電話", "電子郵件", "isgetemail","出生年月日", "自我介紹", "密碼", "連線密碼")

VALUES('ann', '女', '0925-000-000', 'ann@gmail.com', true, '1990-12-31', 'hello', '12345', '67890')


SELECT *
FROM 使用者

SELECT 密碼, 姓名
FROM 使用者
WHERE 電子郵件 = 'ann@gmail.com'

Drop TABLE 使用者