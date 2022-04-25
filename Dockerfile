FROM python:3.8-alpine
WORKDIR /app
COPY . .
RUN ls -lah
RUN cp -r /home/in441/.aws -/
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3","routes.py" ]
