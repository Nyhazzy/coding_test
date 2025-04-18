-- 생일(DATE_OF_BIRTH)이 3월
-- 여성 (GENDER = 'W')
-- ID, 이름, 성별, 생년월일 조회
-- TLNO가 NULL인 경우 제외
-- 회원ID 오름차순
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')
FROM MEMBER_PROFILE
WHERE DATE_OF_BIRTH LIKE '%03%' AND GENDER = 'W' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;