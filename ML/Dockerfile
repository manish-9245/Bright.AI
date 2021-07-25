FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN pip install streamlit

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]

CMD ["app.py"]