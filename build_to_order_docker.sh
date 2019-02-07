docker run -it --rm --name app -v "$PWD":/Lis_Py python:3 python Lis_Py/lis.py || docker start -ia app

docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)