-- 이름(NAME)에 "EL"이 들어가는 개
-- 개의 아이디(ANIMAL_ID)와 이름(NAME)을 조회
-- 이름 순으로 조회 
-- 이름의 대소문자는 구분x
SELECT
    ANIMAL_ID,
    NAME
FROM ANIMAL_INS
WHERE 
    NAME LIKE '%el%' AND
    ANIMAL_TYPE = 'Dog'
ORDER BY NAME ASC;