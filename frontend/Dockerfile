 FROM ubuntu:latest
 RUN apt-get update -y
 RUN apt-get install -y python3-pip python3-dev build-essential
 RUN pip3 install --upgrade pip
 COPY ./service /MythicalMysfitsService
 WORKDIR /MythicalMysfitsService
 RUN pip install -r ./requirements.txt
 EXPOSE 80
 ENTRYPOINT ["python3"]
 CMD ["mythicalMysfitsService.py"]