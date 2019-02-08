docker run -it --rm --name lispy -v "$PWD":/Lis_Py python:3 python Lis_Py/lis.py || docker start -ia lispy

docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
