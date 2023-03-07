FROM python:3.10-slim-buster

LABEL description="My playground api made with FastAPI"

# Set up the dependencies for a Python application,
# And download the Poetry installation script from GitHub piping it to the Python interpreter to run it.
RUN apt-get update \
	&& apt-get install --no-install-recommends -y curl postgresql-client libpq-dev python-dev gcc curl\
	&& curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python

# Set the PATH env. variable to include the /root/.local/bin directory
# extending the previous value of PATH variable rather than completely replacing it.
# This is done to ensure that the executables installed by Poetry are available on the PATH and can be run from the command line.
ENV PATH /root/.local/bin:$PATH

# Copy shell scripts into the current working directory (.) in the image
# and set them up to run by adding execute permissions to the files (+x).

# The entrypoint script, for example, is a script that will run when a container is started from the image,
# and the gunicorn script is used to run a Python application using the Gunicorn server.
COPY backend_entrypoint.sh .
COPY gunicorn_app.sh .
RUN chmod +x backend_entrypoint.sh && chmod +x gunicorn_app.sh

# Set up project dependencies
COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .

# Install dependencies, ensuring that Poetry will not create isolated virtual envs for each project.
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main

# copy source code and configuration files to app dir
COPY alembic.ini .
COPY alembic/ ./alembic
COPY codebase ./codebase
#COPY tests/ ./tests
RUN poetry install


# Set this script as entrypoint for the image.
ENTRYPOINT [ "./backend_entrypoint.sh" ]

# Set the default behavior of container. If no arguments are provided to the docker run command
# when the container is started, this default command will run.
CMD [ "./gunicorn_app.sh" ]
