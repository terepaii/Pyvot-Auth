FROM ubuntu:18.04

COPY . AuthServer/

RUN apt-get update && apt-get install make

WORKDIR AuthServer/

RUN make -f Makefile clean
RUN make -f Makefile install
RUN make -f Makefile tests

EXPOSE 5000/tcp

ENTRYPOINT ["python3", "manage.py",  "run"]