--  flag any participants who score below 50 on their post assessment test
SELECT *
FROM {{ ref('participants_post_assessment') }}
WHERE post_assessment_score < 50