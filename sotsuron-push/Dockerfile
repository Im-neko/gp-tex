FROM python:3.7

WORKDIR /src
COPY ./pip-list.txt ./upload.py ./

RUN pip install --upgrade pip
RUN pip install -r pip-list.txt

CMD ["python", "upload.py"]
