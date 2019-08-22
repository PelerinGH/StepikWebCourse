sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#gunicorn -c --bind='0.0.0.0:8080' hello:app
gunicorn -c --bind='0.0.0.0:8000' --workers=2 --timeout=15 --log-level=debug ask.wsgi:application

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'passwwword';"
mysql -uroot -e "create database stepik_web"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
mysql -uroot -e "FLUSH PRIVILEGES;"
sudo python ~/web/ask/manage.py makemigrations qa
sudo python ~/web/ask/manage.py migrate