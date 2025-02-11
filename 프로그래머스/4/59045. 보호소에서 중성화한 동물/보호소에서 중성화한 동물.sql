-- 들어올 때는 중성화 x, 나갈 때는 중성화
-- ID, 생물 종, 이름 조회
-- ID 순으로 조회
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_OUTS AS OUTS
LEFT JOIN ANIMAL_INS AS INS ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE (INS.SEX_UPON_INTAKE = 'Intact Male' AND OUTS.SEX_UPON_OUTCOME= 'Neutered Male') OR (INS.SEX_UPON_INTAKE = 'Intact Female' AND OUTS.SEX_UPON_OUTCOME = 'Spayed Female')
ORDER BY INS.ANIMAL_ID;