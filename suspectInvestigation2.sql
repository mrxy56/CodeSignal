# 1. There are two Bill Greens, so an id must be included.
CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, name, surname
	FROM Suspect
	WHERE (id, name, surname) NOT IN (
		SELECT id, name, surname
		FROM Suspect
		WHERE height > 170 AND LEFT(name, 1) = 'B' AND LENGTH(surname) = 5 AND surname LIKE 'Gre%n'
	);
END