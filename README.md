sudo apt-get install python3
sudo apt install python3-pip
pip install fastapi
pip install "uvicorn[standard]"
git clone https://github.com/Prateek-9814/Frame.git
cd Frame/
sh install-docker.sh
sudo usermod -aG docker $USER
newgrp docker 
docker network create -d bridge python 
pip install -r requirements.txt 

Check ip:8000/docs in web 

Build the docker image 

docker run -d  --network python -e POSTGRES_PASSWORD=123456789 --name abc postgres
docker run -it -p 8000:8000 --network python -e DATABASE_URL=postgresql+psycopg2://postgres:123456789@abc prateek9814/book
