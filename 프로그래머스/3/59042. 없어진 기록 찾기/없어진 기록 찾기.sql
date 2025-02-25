-- ANIMAL_INS 들어온 기록, ANIMAL_OUTS 입양 보낸 기록
-- 입양간 기록은 있는데, 보호소에 들어온 기록이 없는
-- 동물 ID와 이름 조회
-- ID 순으로 정렬
SELECT
    OUTS.ANIMAL_ID,
    OUTS.NAME
FROM ANIMAL_OUTS AS OUTS
LEFT JOIN ANIMAL_INS AS INS ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY 1;
