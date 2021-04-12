FROM python:3

WORKDIR /usr/src/app
COPY ./src .

RUN pip install --upgrade pip && \
	pip install -r requirements.txt

CMD ["anki.py"]
ENTRYPOINT ["python3"]
