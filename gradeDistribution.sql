CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT Name, ID
	FROM Grades
	WHERE FINAL > (0.25 * Midterm1 + 0.25 * Midterm2 + 0.5 * Final) AND FINAL > (0.5 * Midterm1 + 0.5 * Midterm2)
	ORDER BY LEFT(Name, 3) ASC, ID ASC;
END