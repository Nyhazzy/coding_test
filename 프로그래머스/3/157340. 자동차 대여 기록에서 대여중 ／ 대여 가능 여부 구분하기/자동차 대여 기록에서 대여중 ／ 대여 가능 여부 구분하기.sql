-- 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시
-- 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼
-- 컬럼명: AVAILABILITY)을 추가
SELECT CAR_ID,
CASE 
    WHEN MAX(START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16') THEN '대여중'
    ELSE '대여 가능'
END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;