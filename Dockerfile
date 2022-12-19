FROM python:3.9
WORKDIR /gpt
COPY ./core/ /gpt
COPY ./resources /gpt
COPY . /gpt
#CMD ["source venv/Scripts/activate"]
CMD ["python", "main.py"]