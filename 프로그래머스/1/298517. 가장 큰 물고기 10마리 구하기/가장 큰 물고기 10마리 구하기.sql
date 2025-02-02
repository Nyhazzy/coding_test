-- 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 NULL 이며, LENGTH 에 NULL 만 있는 경우는 없습니다
-- FISH_INFO 테이블에서 가장 큰 물고기 10마리의 ID와 길이를 출력
-- 길이를 기준으로 내림차순 정렬

SELECT
    ID,
    LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID ASC
LIMIT 10;

