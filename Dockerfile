# needs work -- from project 2
FROM python:latest
ADD src/app /src/app
ADD src/instance /src/instance
ADD src/static /src/static
ADD src/instance /src/instance
ADD src/templates /src/templates
COPY requirements.txt /tmp
WORKDIR /src
EXPOSE 5000
RUN pip install -r /tmp/requirements.txt
ENV FLASK_APP=/src/app
CMD ["flask", "run", "-h", "0.0.0.0"]
# docker build -t proj3 .
# docker run -i --name proj3 --publish 5000:5000 --rm proj3