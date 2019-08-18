sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 wsgi