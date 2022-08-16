
"Strings for querying the database"

query_mag = f"""
SELECT f.AuthorId
    , f.firstname
    , f.lastname
    , CASE TRIM(SUBSTR(f.middle_lastname, 1, f.l_fullname - f.l_firstname - f.l_lastname - 1)) 
        WHEN 
            "" THEN NULL 
            ELSE TRIM(SUBSTR(f.middle_lastname, 1, f.l_fullname - f.l_firstname - f.l_lastname - 1)) 
        END as middlename 
    , g.main_us_institutions_year
    , g.all_us_institutions_year
    , f.YearFirstPub || ";" || f.YearLastPub AS year_range 
FROM (
    SELECT a.AuthorId
        , a.YearFirstPub 
        , a.YearLastPub 
        , a.FirstName AS firstname
        , REPLACE(b.NormalizedName, RTRIM(b.NormalizedName, REPLACE(b.NormalizedName, " ", "")), "") AS lastname 
        , TRIM(SUBSTR(b.NormalizedName, length(a.FirstName) + 1)) AS middle_lastname 
        , length(b.NormalizedName) as l_fullname 
        , length(a.FirstName) as l_firstname
        , length(REPLACE(b.NormalizedName, RTRIM(b.NormalizedName, REPLACE(b.NormalizedName, " ", "")), "")) as l_lastname
    FROM author_sample AS a
    INNER JOIN (
        SELECT AuthorId, NormalizedName
        FROM Authors
    ) AS b USING(AuthorId)
    INNER JOIN (
        -- ## mark: different from linking graduates. filter on field0
        SELECT AuthorId, NormalizedName
        FROM author_fields c
        INNER JOIN (
            SELECT FieldOfStudyId, NormalizedName
            FROM FieldsOfStudy
        ) AS d USING(FieldOfStudyId)
        WHERE FieldClass = 'main'
            AND FieldOfStudyId = 121332964
    ) AS e USING(AuthorId)
) AS f
LEFT JOIN (
    SELECT AuthorId
            , main_us_institutions_year
            , all_us_institutions_year
    FROM author_info_linking
) AS g USING(AuthorId)
WHERE length(f.firstname) > 1 
    AND f.firstname IS NOT NULL 
    AND length(f.lastname) > 1
    AND f.lastname IS NOT NULL 
    AND f.YearLastPub >= 1980 
    AND f.YearFirstPub <= 2022
    AND g.main_us_institutions_year IS NOT NULL 
"""


query_nsf = f""" 
SELECT a.GrantID || "_" || c.author_position AS grantid_personpos
    , CAST(SUBSTR(a.Award_AwardEffectiveDate, 7, 4) AS INT) AS year_range
    , c.firstname, c.lastname, c.middlename
    , CAST(SUBSTR(a.Award_AwardEffectiveDate, 7, 4) AS INT) || "//" || b.institution AS main_us_institutions_year
    , CAST(SUBSTR(a.Award_AwardEffectiveDate, 7, 4) AS INT) || "//" || b.institution AS all_us_institutions_year
FROM NSF_MAIN as a 
INNER JOIN (
    SELECT GrantID, Name AS institution
    FROM NSF_Institution
    WHERE Position = 0 -- take the first reported 
) b 
USING (GrantID)
INNER JOIN (
    SELECT GrantID
        , FirstName AS firstname
        , LastName AS lastname
        , PIMidInit AS middlename 
        , Position as author_position
    FROM NSF_Investigator
    WHERE RoleCode = 'principal investigator'
) c
USING (GrantID)
WHERE AWARD_TranType = 'grant' 
    AND AWARD_Agency = 'nsf' 
    AND a.AwardInstrument_Value IN ('standard grant', 'continuing grant')
    AND a.Organization_Directorate_ShortName = 'MATHEMATICAL & PHYSICAL SCIEN'
    AND c.lastname != 'data not available'
    AND c.firstname IS NOT NULL 
"""
