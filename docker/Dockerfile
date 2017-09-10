FROM python:3

WORKDIR /usr/src/app
ENV APPLICATION_DIR=pyhton-list-lib

#COPY ${APPLICATION_DIR}/requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY ${APPLICATION_DIR} .

ARG arg=10
RUN if [ "x$arg" = "x" ] ; then echo " echo Argument not provided">file.txt ; else echo "Argument is $arg">file.txt ; fi

#cd pyinterval
#RUN python setup.py install


#CMD [ "python", "hello.py" ]
#docker run -it --rm --name docker localhost:8123/docker-python:1.0-SNAPSHOT /bin/bash
