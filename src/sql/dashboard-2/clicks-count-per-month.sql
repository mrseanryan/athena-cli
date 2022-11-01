-- === Total Clicks per Month, by version ===
--
SELECT year_and_month, count(click_id) as Clicks, min(application_version_int) / 100 as version
FROM
(
  SELECT application_version_int, year_and_month, page_id
  FROM
  (
    SELECT
    CASE
      WHEN application_version_short = '1.0.'
        THEN 100
      WHEN application_version_short = '1.1.'
        THEN 101
      WHEN application_version_short = '1.2.'
        THEN 102
      WHEN application_version_short = '1.3.'
        THEN 103
      WHEN application_version_short = '1.4.'
        THEN 104
      WHEN application_version_short = '1.5.'
        THEN 105
      WHEN application_version_short = '1.6.'
        THEN 106
      WHEN application_version_short = '1.7.'
        THEN 107
      WHEN application_version_short = '1.8.'
        THEN 108
      WHEN application_version_short = '1.9.'
        THEN 109
      ELSE
        CAST(application_version_short as DOUBLE) * 100
    END AS application_version_int,
    year_and_month,
    click_id
    FROM
    (
      SELECT
      SUBSTRING(CAST(timestamp AS VARCHAR) FROM 1 FOR 7) AS year_and_month,
      SUBSTRING(application_version FROM 1 FOR 4) application_version_short,
      *
      from my_database.my_data
      WHERE event = 'USER_CLICKED'
      AND timestamp >= date('2022-01-01')
      --LIMIT 50
    )
  )
  GROUP BY year_and_month, click_id, application_version_int
)
GROUP BY year_and_month, application_version_int
ORDER BY year_and_month, application_version_int
