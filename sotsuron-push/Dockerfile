FROM python:3.7

WORKDIR /src
COPY ./pip-list.txt ./upload.py ./

RUN pip install --upgrade pip
RUN pip install -r pip-list.txt

ARG LOGIN_ID
ARG LOGIN_PASS
ARG FILE_TITLE

ENV LOGIN_ID $LOGIN_ID
ENV LOGIN_PASS $LOGIN_PASS
ENV FILE_TITLE $FILE_TITLE

CMD ["python", "upload.py"]
