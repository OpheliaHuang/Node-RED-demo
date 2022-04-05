
sudo docker stop flask && sudo docker rm flask 

echo "I will start the docker app now"

sudo docker build -t flask-app:latest .

#Run the Docker container using the command shown below.


sudo docker run --name flask -p 5000:5000 flask-app


echo The application will be accessible at http:127.0.0.1:5000
