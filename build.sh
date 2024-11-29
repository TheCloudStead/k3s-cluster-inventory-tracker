sudo docker build -t <image_name>:latest .
sudo docker tag <image_name>:latest localhost:5000/<image_name>:latest
sudo docker push <registy_ip>:<registry_port>/<image_name>:latest