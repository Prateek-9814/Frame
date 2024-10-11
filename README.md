# Include the image
![image](https://github.com/Prateek-9814/Frame/assets/130494326/0482c08c-9669-47a1-8814-bfb6661ff56f)

# Commands for setting up the environment
sudo apt-get install python3
sudo apt install python3-pip
pip install fastapi
pip install "uvicorn[standard]"

# Clone your repository
git clone https://github.com/Prateek-9814/Frame.git
cd Frame/

# Install Docker and add current user to the Docker group
sh install-docker.sh
sudo usermod -aG docker $USER
newgrp docker 

# Create a Docker network
docker network create -d bridge python 

# Install Python dependencies
pip install -r requirements.txt 

# Check the application at ip:8000/docs in the web browser

# Build and run Docker images
docker run -d --network python -e POSTGRES_PASSWORD=123456789 --name abc postgres
docker run -it -p 8000:8000 --network python -e DATABASE_URL=postgresql+psycopg2://postgres:123456789@abc prateek9814/book
