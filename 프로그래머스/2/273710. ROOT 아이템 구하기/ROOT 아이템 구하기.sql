-- ROOT 아이템을 찾아 (ROOT 아이템은 PARENT_ITEM_ID)
-- ITEM_ID, ITEM_NAME을 출력
-- 아이템 ID를 기준으로 오름차순
SELECT
    INFO.ITEM_ID, INFO.ITEM_NAME
FROM ITEM_INFO AS INFO
JOIN ITEM_TREE AS TREE ON INFO.ITEM_ID = TREE.ITEM_ID
WHERE TREE.PARENT_ITEM_ID IS NULL
ORDER BY 1 ASC;