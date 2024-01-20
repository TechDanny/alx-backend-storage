-- This script creates a stored procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    UPDATE users AS pips,
		(SELECT pips.id, SUM(score * weight) / SUM(weight) AS X
		FROM users AS pips
		JOIN corrections AS n ON pips.id=n.user_id
		JOIN projects AS p ON n.project_id=p.id
		GROUP BY pips.id)
		AS D
		SET pips.average_score = D.X
		WHERE pips.id = D.id;
END
$$
DELIMITER ;
