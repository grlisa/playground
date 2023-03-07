#!/bin/sh
set -e

# Do a pre-check and wait for database network connection.
if [ ! -z "${DB_URI}" ]
then
		>&2 echo "*** DB setup ***"

		# parse DB_URI
		uri_parts="$(echo $DB_URI | grep :// | cut -d@ -f2)"
		DB_HOST="$(echo $uri_parts | cut -d: -f1)"
		DB_PORT="$(echo $uri_parts | cut -d: -f2 | cut -d/ -f1)"
		POSTGRES_DB="$(echo $uri_parts | cut -d/ -f2)"

		tms=$(date '+%Y-%m-%d %H:%M:%S')
		echo "${tms} | Using DB connection with host: $DB_HOST, port: $DB_PORT, db: $POSTGRES_DB"
		echo "${tms} | Checking DB connectivity ..."

		timer="2"
		while ! pg_isready -h ${DB_HOST} -p ${DB_PORT} > /dev/null 2> /dev/null;
		do
			tms=$(date '+%Y-%m-%d %H:%M:%S')
			echo "${tms} | Waiting for DB to accept connections (sleeping ${timer}s) ..."
			sleep $timer
		done

		tms=$(date '+%Y-%m-%d %H:%M:%S')
		echo "${tms} | Running alembic for DB version migrations ..."
		poetry run alembic upgrade head

		>&2 echo "*** DB setup finished ***"

fi

# load from freshly-created .env, if exists
if [ -f .env ]
then
	ENVVARS=$(cat .env | sed 's/#.*//g' | sed '/^$/d' | xargs -0)
	set -o allexport
	source .env
	set +o allexport
fi

# and run command
exec "$@"
