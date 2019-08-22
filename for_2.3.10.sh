sudo /etc/init.d/mysql start
#sudo systemctl start mariadb
#mysql -uroot -e "DROP DATABASE IF EXISTS askappdb;"
#mysql -uroot -e "DROP USER 'askapp'@'localhost';" mysql
CREATE DATABASE askappdb;
CREATE USER 'askapp'@'localhost' IDENTIFIED BY 'passwrd123';
GRANT ALL PRIVILEGES ON askappdb.* TO 'askapp'@'localhost';
FLUSH PRIVILEGES;