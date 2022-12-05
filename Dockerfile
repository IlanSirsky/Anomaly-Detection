FROM python:3.9.13

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY ./app.py .

COPY ./model/finalized_model.pkl ./model/finalized_model.pkl

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]