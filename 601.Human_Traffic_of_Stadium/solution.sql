-- Write your PostgreSQL query statement below
WITH rolling_min AS (
    SELECT
        id,
        MIN(people) OVER (
            ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING
        ) AS min_people,
        MIN(people) OVER (
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS min_people_back
    FROM Stadium
), result AS (
    SELECT *
    FROM Stadium
    WHERE id IN (
        SELECT id
        FROM rolling_min
        WHERE
            min_people >= 100
            OR min_people_back >= 100
    )
), filtred_ids AS (
    SELECT id
    FROM result
)
SELECT *
FROM result
WHERE
    (
        id+1 IN (SELECT * FROM filtred_ids)
        AND (
            id + 2 IN (SELECT * FROM filtred_ids)
            OR id - 1 IN (SELECT * FROM filtred_ids)
        )
    )
    OR (
        id - 1 IN (SELECT * FROM filtred_ids)
        AND id - 2 IN (SELECT * FROM filtred_ids)
    )
ORDER BY visit_date;
