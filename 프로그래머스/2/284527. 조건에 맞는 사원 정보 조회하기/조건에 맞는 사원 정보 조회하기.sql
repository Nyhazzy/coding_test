-- 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회
-- 2022년도의 평가 점수는 상,하반기 점수의 합 -> EMP_NO 로 묶어서 상반기 하반기 점수 합산
SELECT
    SUM(GR.SCORE) AS SCORE,
    EM.EMP_NO,
    EM.EMP_NAME,
    EM.POSITION,
    EM.EMAIL
FROM HR_EMPLOYEES AS EM
JOIN HR_GRADE AS GR ON EM.EMP_NO = GR.EMP_NO
GROUP BY GR.EMP_NO
ORDER BY SCORE DESC
LIMIT 1;
