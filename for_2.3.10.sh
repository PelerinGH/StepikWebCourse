sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'passwwword';"
mysql -uroot -e "create database stepik_web"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate