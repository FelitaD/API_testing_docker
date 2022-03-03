FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests==2.7.0
COPY authorization/test_authorization.py /tests/test_authorization.py
COPY template/test_template.py /tests/template/test_template.py
WORKDIR /tests/
EXPOSE 8000
CMD python3 test_authorization.py