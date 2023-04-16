--Running this script returns results for all the queries in one transaction
--and will display all to the terminal window.
--The \! echo lines will print readable headers above each result set to give clear detail on which dataset
--relates to which exercise.

USE COMPANY1;

--Select all records from EMP
\! echo " ";
\! echo "##################################################################################";
\! echo "Select all records from EMP (Reference).";
\! echo "##################################################################################";
\! echo " ";
SELECT * FROM EMP;

--Select all records from DEPT
\! echo " ";
\! echo "##################################################################################";
\! echo "Select all records from DEPT (Reference).";
\! echo "##################################################################################";
\! echo " ";
SELECT * FROM DEPT;

--List all Employees whose salary is between 1,000 AND 2,000
--Show the Employee Name, Department and Salary.
--The code returns specific fields form the EMP table and uses a join on the DEPT 
--table to return the dept name instead of the number.
\! echo " ";
\! echo "##################################################################################";
\! echo "Exercise 1 - List all Employees whose salary is between 1,000 AND 2,000";
\! echo "listing the Name, department and salary.";
\! echo "##################################################################################";
\! echo " ";
SELECT E.ENAME AS 'Name', D.DNAME AS 'Department', E.SAL AS 'Salary' 
FROM EMP E
INNER JOIN DEPT D
ON E.DEPTNO = D.DEPTNO
WHERE SAL BETWEEN 1000.00 AND 2000.00;

--Count the number of people in department 30 who receive a salary 
--and the number of people who receive a commission.
--The code uses count functions to return the actual amounts.
\! echo " ";
\! echo "##################################################################################";
\! echo "Exercise 2 - Count the number of people in department 30 who receive a salary";
\! echo "and the number of people who receive a commission.";
\! echo "##################################################################################";
\! echo " ";
SELECT COUNT(CASE WHEN SAL > 0 THEN 1 END) AS 'Employees on Salary - Dept 30', 
COUNT(CASE WHEN COMM > 0 THEN 1 END) as 'Employees on commission - Dept 30' 
FROM EMP
WHERE DEPTNO = 30;

--Find the name and salary of employees in Dallas.
--The code uses a join on both tables and the where clause is explicit naming the department. 
\! echo " ";
\! echo "##################################################################################";
\! echo "Exercise 3 - Find the name and salary of employees in Dallas.";
\! echo "##################################################################################";
\! echo " ";
SELECT E.ENAME AS 'Name', E.SAL AS 'Salary' 
FROM EMP E
INNER JOIN DEPT D
ON E.DEPTNO = D.DEPTNO
WHERE D.LOC = 'DALLAS';

--List all departments that do not have any employees.
--The code uses a inline sql statement in the where clause to 
--return departments that do not appear in the EMP table.
\! echo " ";
\! echo "##################################################################################";
\! echo "Exercise 4 - List all departments that do not have any employees.";
\! echo "##################################################################################";
\! echo " ";
SELECT DNAME AS 'Department with no employees' 
FROM DEPT 
WHERE DEPTNO NOT IN(SELECT DEPTNO FROM EMP);

--List the department number and average salary of each department.
--The code uses the AVG function to calculate the average salaray and groups all the values by DEPTNO.
\! echo " ";
\! echo "##################################################################################";
\! echo "Exercise 5 - List the department number and average salary of each department.";
\! echo "##################################################################################";
\! echo " ";
SELECT DEPTNO AS 'Dept Number', AVG(SAL) AS 'Average Salary' 
FROM EMP
GROUP BY DEPTNO;