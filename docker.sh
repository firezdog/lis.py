docker build -t lis.py .
docker run -it --rm --name lispy-running lis.py

# https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/
# https://stackoverflow.com/questions/48047810/cannot-connect-to-the-docker-daemon-on-bash-on-ubuntu-windows
# https://stackoverflow.com/questions/26424338/docker-daemon-config-file-on-boot2docker-docker-machine-docker-toolbox/26781047#26781047