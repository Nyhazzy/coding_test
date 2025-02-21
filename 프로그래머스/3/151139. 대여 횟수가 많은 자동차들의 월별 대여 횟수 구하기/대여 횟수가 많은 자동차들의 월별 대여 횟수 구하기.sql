-- 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인
-- 해당 기간 동안의 월별 (월별 그룹화?) 자동차 ID 별 총 대여 횟수 : RECORDS
-- 월을 기준으로 오름차순 정렬, 월이 같다면 자동차 ID 기준으로 내림차순
-- 특정 월의 총 대여 횟수가 0인 경우에는 제외

SELECT
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT 
        CAR_ID      
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE MONTH(START_DATE) BETWEEN 8 AND 10
      GROUP BY CAR_ID
      HAVING COUNT(*) >= 5) AND MONTH(START_DATE) BETWEEN 8 AND 10
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;