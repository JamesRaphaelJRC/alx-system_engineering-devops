-- Creates a user 'holberton_user' with host name set to loccalhost and 
-- Password projectcorrection280hbtn
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
