-- This script  creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. 
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT AVG(score) FROM corrections AS X WHERE X.user_id = user_id);
    UPDATE users set average_score = avg_score WHERE id = user_id;
END
$$
DELIMITER ;