#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "<!DOCTYPE html>
<html>
  <head>
	<meta charset='UTF-8'>
	<title>Test</title>
  </head>
  <body>
    <p>Nginx html test file</p>
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0
