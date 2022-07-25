FROM python:3.9

RUN apt-get update && apt-get install -y wget && apt-get clean

# Install dockerize to check other dependencies
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Create appuser & appgroup
ARG USER_ID
ARG GROUP_ID

RUN groupadd -g ${GROUP_ID} appgroup &&\
    useradd -l -u ${USER_ID} -g appgroup appuser &&\
    install -d -m 0755 -o appuser -g appgroup /home/appuser

# Create shared volumes in order to setup initial permissions & ownership
RUN mkdir -p /logs && chown -R appuser:appgroup /logs && chmod -R 1777 /logs
RUN mkdir -p /static && chown -R appuser:appgroup /static && chmod -R 1777 /static

# Prepare workdir
ARG PROJECT_NAME

RUN mkdir ${PROJECT_NAME} && chown -R appuser:appgroup /${PROJECT_NAME}
WORKDIR ${PROJECT_NAME}


# Install python project dependencies
ARG PROJECT_DJANGO_DIR

COPY --chown=appuser:appgroup requirements/requirements-app.txt /${PROJECT_NAME}/

RUN apt-get update && apt-get install -y python3-pip
RUN python3.9 -m pip install --upgrade pip
RUN pip3.9 install -r requirements-app.txt

# Copy sources
COPY --chown=appuser:appgroup docker/app/entrypoints /entrypoints
RUN chmod gu+x /entrypoints/* && chown appuser:appgroup /entrypoints

COPY --chown=appuser:appgroup ${PROJECT_NAME}/${PROJECT_DJANGO_DIR}/ /${PROJECT_NAME}

USER appuser

ENTRYPOINT ["/entrypoints/entrypoint.sh"]