SELECT
    participant_id,
    pre_assessment_score,
    post_assessment_score,
    pre_confidence_level,

    -- calculate improvement
    round(((post_assessment_score - pre_assessment_score)/pre_assessment_score) * 100,2) AS percentage_improvement,

    -- calculate post confidence level based on thresholds
    CASE
        WHEN post_assessment_score <= 50 THEN 'Beginner'
        WHEN post_assessment_score <= 75 THEN 'Intermediate'
        ELSE 'Advanced'
    END AS post_confidence_level
FROM
    {{ ref('participants_performance_metric') }}
