FROM python:3.10.2-slim

RUN useradd -ms /bin/bash python

RUN pip install pdm

USER python

WORKDIR /home/python/app

ENV PYTHON_PACKAGES=/home/python/app/__pypackages__/3.10
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

ENV PATH $PATH:${PYTHON_PACKAGES}/bin

CMD [ "tail", "-f", "/dev/null" ]