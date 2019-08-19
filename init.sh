sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#gunicorn -c --bind='0.0.0.0:8080' hello:app
gunicorn -c --bind='0.0.0.0:8000' --workers=2 --timeout=15 --log-level=debug ask.wsgi:application