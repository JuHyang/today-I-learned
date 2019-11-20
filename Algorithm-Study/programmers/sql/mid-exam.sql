-- 5.13
-- a
INSERT INTO STUDENT VALUES ('Johnson', 25, 1, 'Math');

-- b
UPDATE SET Grade = 2 FROM STUDENT WHERE Name = 'Smith';

-- c
INSERT INTO 과목 VALUES ('Knowege Engineering', 'CS4390', 3, 'CS');

-- d
DELETE FROM STUDENT WHERE Name = 'Smith' AND Number = 17;

-- 6.7
-- a 
SELECT fname, lname FROM EMPLYEE WHERE Dno IN (SELECT Dno FROM EMPLOYEE WHERE Salary IN (SELECT MAX(Salary) FROM EMPLOYEE));

-- b
SELECT fname, lname FROM EMPLOYEE WHERE Super_ssn IN (SELECT Ssm FROM EMPLOYEE WHERE Super_ssn = '888665555');

-- c
SELECT fname, lname FROM EMPLOYEE WHERE Salary >= 10000 + (SELECT MIN(Salary) FROM EMPLOYEE);

-- 6.5
-- a
SELECT Dname, COUNT (*) FROM DEPARTMENT JOIN EMPLOYEE ON Dnumber = Dno GROUP BY dname HAVING AVG(Salary) >= 30000;


-- b
SELECT Dname, COUNT (*) FROM DEPARTMENt JOIN EMPLOYEE ON Dnumber = Dno WHERE Sex = 'M' AND Salary >= 30000 GROUP BY dname;

-- 6.6
-- a
SELECT Name, Major FROM STUDENT, GRADE_REPORT WHERE STUDENT.Stdent_number = GRADE_REPORT.Student_number AND 


-- 6.8
-- a
CREATE VIEW MANAGERS
AS SELECT Dname, Fname, Salary
FROM DEPARTMENT, EMPLOYEE
WHERE Mgr_ssn = Ssn;

-- b
CREATE VIEW RESEARCH_PERSON
AS SELECT E1.Fname AS Name, E2.Fname AS Super_Name, E1.Salary
FROM EMPLOYEE as E1, EMPLOYEE as E2, DEPARTMENT
WHERE E1.Dno IN (SELECT Dnumber FROM DEPARTMENT WHERE Dname='Research') AND E2.Ssn = E1.Super_ssn;

-- c
CREATE VIEW PROJECTS
AS SELECT Pname, Dname, COUNT(Essn), SUM(Hours)
FROM Project, Department, WORKS_ON
WHERE Dnum = Dnumber AND Pnumber = Pno
GROUP BY Pname;

-- d
CREATE VIEW ASDF
AS SELECT Pname, Dname, COUNT(Essn), SUM(Hours)
FROM PROJECT, DEPARTMENT, WORKS_ON
WHERE Dnum = Dnumber AND Pnumber = Pno
GROUP BY Pname
HAVING COUNT(ESsn) >= 1;

