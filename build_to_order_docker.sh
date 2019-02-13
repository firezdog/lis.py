docker run -it --rm --name lispy -v "$PWD":/Lis_Py python:3 python Lis_Py/lis.py || docker start -ia lispy

# on WSL with docker running in windows, $PWD will not work and must be set to the same as $PWD from docker quick-start,
# viz. docker run -it --rm --name lispy -v /c/Users/firez/Documents/Development/lis.py:/Lis_Py python:3 python Lis_Py/lis.py || docker start -ia lispy

docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
