-- 부서별로 부서 ID, 영문 부서명, 평균 연봉을 조회 , 어떻게 JOIN?
-- 평균연봉은 소수점 첫째 자리에서 반올림 컬럼명은 AVG_SA
-- 부서별 평균 연봉을 기준으로 내림차순 정렬
SELECT 
    DE.DEPT_ID,
    DE.DEPT_NAME_EN,
    ROUND(AVG(SAL), 0) AS AVG_SAL
FROM HR_EMPLOYEES AS EM
LEFT JOIN HR_DEPARTMENT AS DE ON EM.DEPT_ID = DE.DEPT_ID
GROUP BY EM.DEPT_ID
ORDER BY AVG_SAL DESC;