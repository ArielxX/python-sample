FROM python:3.10

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 9093

CMD [ "python3", "main.py"]