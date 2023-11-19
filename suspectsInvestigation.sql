CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, name, surname
	FROM Suspect
	WHERE height <= 170 AND LEFT(name, 1) = 'B' AND surname LIKE "Gre%n" AND LENGTH(surname) = 5
	ORDER BY id ASC;
END