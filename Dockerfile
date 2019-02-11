FROM python:3

WORKDIR $(pwd):/home/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./lis.py" ]
