-- Write your PostgreSQL query statement below
WITH banned_users AS (
    SELECT users_id
    FROM Users
    WHERE banned::TEXT = 'Yes'
), trips_with_no_banned_users AS (
    SELECT *
    FROM Trips
    WHERE
        request_at::TIMESTAMP
            BETWEEN '2013-10-01'::TIMESTAMP AND '2013-10-03'::TIMESTAMP
        AND client_id NOT IN (SELECT * FROM banned_users)
        AND driver_id NOT IN (SELECT * FROM banned_users)
)
SELECT
    request_at AS "Day",
    round(
        SUM(
            CASE WHEN status::TEXT = 'completed' THEN 0 ELSE 1 END
        )::NUMERIC / COUNT(*),
        2
    )  AS "Cancellation Rate"
FROM trips_with_no_banned_users
GROUP BY request_at;
