-- This script creates a stored procedure
DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    UPDATE users
   	SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id=users.id)
	WHERE id=user_id;
END;
|
DELIMITER ;
