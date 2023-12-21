FROM python
COPY db_configuration .
COPY entities .
COPY db_configuration.xml .
COPY *.py .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]