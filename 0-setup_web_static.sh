#!/usr/bin/env bash
# sets up nginx and configures folders for static files

sudo apt update && sudo apt upgrade

sudo apt install -y nginx

if [ ! -d "/data/" ]; then
        sudo mkdir /data/
fi

if [ ! -d "/data/web_static/" ]; then
        sudo mkdir /data/web_static/
fi

if [ ! -d "/data/web_static/releases/" ]; then
        sudo mkdir /data/web_static/releases/
fi

if [ ! -d "/data/web_static/shared/" ]; then
        sudo mkdir /data/web_static/shared/
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
        sudo mkdir /data/web_static/releases/test/
fi

if [ ! -f "/data/web_static/releases/test/index.html" ]; then
        sudo touch /data/web_static/releases/test/index.html
fi

sudo cat << EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo cat << EOF > /etc/nginx/sites-available/default
server {
        location /hbnb_static/ {
                alias /data/web_static/current/;
        }
}
EOF

sudo service nginx restart
sudo chmod -R 755 /data
sudo chown -R ubuntu:ubuntu /data
