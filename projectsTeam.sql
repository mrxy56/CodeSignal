CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT name
	FROM projectLog
	GROUP BY name
	ORDER BY name ASC;
END