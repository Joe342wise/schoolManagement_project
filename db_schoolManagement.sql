create database schoolManagementSystem;
use schoolManagementSystem;

-- Students Table
CREATE TABLE tblStudents (
  stdIdpk INT PRIMARY KEY AUTO_INCREMENT,
  stdFirstName VARCHAR(50) NOT NULL,
  stdLastName VARCHAR(50) NOT NULL,
  stdDateOfBirth DATE,
  stdGradeLevel INT,
  stdEmergencyContactInfomation VARCHAR(255)
);

-- Teachers Table
CREATE TABLE tblTeachers (
  techIdpk INT PRIMARY KEY AUTO_INCREMENT,
  techFirstName VARCHAR(50) NOT NULL,
  techLastName VARCHAR(50) NOT NULL,
  techSubjectTought VARCHAR(100),
  techEmail VARCHAR(100) NOT NULL,
  techPhoneNumber VARCHAR(20)
);

-- Courses Table
CREATE TABLE tblCourses (
  cosIdpk INT PRIMARY KEY AUTO_INCREMENT,
  cosName VARCHAR(100) NOT NULL,
  techIdpk INT,
  FOREIGN KEY (techIdpk) REFERENCES tblTeachers(techIdpk)
);

-- Enrollments Table
CREATE TABLE tblEnrollments (
  ermIpk INT PRIMARY KEY AUTO_INCREMENT,
  stdIdpk INT,
  cosIdpk INT,
  FOREIGN KEY (stdIdpk) REFERENCES tblStudents(stdIdpk),
  FOREIGN KEY (cosIdpk) REFERENCES tblCourses(cosIdpk)
);

-- Grades Table
CREATE TABLE tblGrades (
  grdIdpk INT PRIMARY KEY AUTO_INCREMENT,
  stdIdpk INT,
  cosIdpk INT,
  grade DECIMAL(5,2), -- This allows for grades with two decimal places (e.g., 3.75)
  grdDate DATE,
  FOREIGN KEY (stdIdpk) REFERENCES tblStudents(stdIdpk),
  FOREIGN KEY (cosIdpk) REFERENCES tblCourses(cosIdpk)
);

-- Users Table
CREATE TABLE tblUsers (
  userIdpk INT PRIMARY KEY AUTO_INCREMENT,
  userName VARCHAR(255) NOT NULL,
  Email VARCHAR(100) NOT NULL UNIQUE,
  userPassword VARCHAR(255) NOT NULL,
  userRole ENUM('admin', 'teacher', 'student') NOT NULL,
  IsActive BOOLEAN DEFAULT TRUE
);
