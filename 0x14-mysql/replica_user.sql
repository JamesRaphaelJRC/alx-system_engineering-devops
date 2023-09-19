-- Creates a new user replica_user with hostname '%'
-- replica_user to have the appropriate permissions to replicate yout primary
-- MySQL server
-- Grants SELECT privileges on the mysql.user table to holberton_user in order
-- to check that replica_user was created with the correct permissions.
CREATE USER 'replica_user'@'%';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
