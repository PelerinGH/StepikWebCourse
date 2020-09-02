sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#gunicorn -c --bind='0.0.0.0:8080' hello:app
gunicorn --bind='0.0.0.0:8000' --workers=2 --timeout=15 --log-level=debug ask.wsgi:application


sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
sudo python3 ~/web/ask/manage.py makemigrations
sudo python3 ~/web/ask/manage.py migrate
