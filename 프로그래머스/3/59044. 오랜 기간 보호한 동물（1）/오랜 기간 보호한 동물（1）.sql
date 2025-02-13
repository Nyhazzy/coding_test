-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리 
-- 이름과 보호 시작일을 조회
-- 보호 시작일 순으로 조회
SELECT
    I.NAME,
    I.DATETIME
FROM ANIMAL_INS AS I
LEFT JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY 2
LIMIT 3;