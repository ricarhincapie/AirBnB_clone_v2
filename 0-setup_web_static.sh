#!/usr/bin/env bash
# Script to get a machine ready for static deploy with Fabric and Nginx

sudo apt-get -y update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'

sudo mkdir -p ~/data/web_static/{releases/test,shared}
str_html=$'<html>\n\t<head>\n\t</head>\n\t<body>\n\tHolberton School\n\t</body>\n</html>'
echo "$str_html" | sudo tee ~/data/web_static/releases/test/index.html
sudo ln -s ~/data/web_static/releases/test/ ~/data/web_static/current
sudo chown -R ubuntu:ubuntu ~/data/
sudo sed -i '/listen 80 default_server/a \\n\tlocation /hbnb_static/ {\n\t\talias /home/ubuntu/data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
