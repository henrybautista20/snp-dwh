sudo apt update
sudo apt install --reinstall python3-apt python3-minimal
sudo apt install --reinstall python3-cffi libffi-dev python3-cryptography
sudo apt --fix-broken install
pip3 install --upgrade --force-reinstall cffi cryptography


## restart docker 
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
docker system prune -a --volumes -f
docker ps -a

# solve problen in local sudo chmod 666 /var/run/docker.sock
