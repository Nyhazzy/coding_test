-- 동물의 생물 종, 이름, 성별 및 중성화 여부 조회
-- 아이디 순
-- 이름이 NULL인 것을 No name으로 변경
SELECT
    ANIMAL_TYPE,
    COALESCE(NAME, 'No name') AS NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
