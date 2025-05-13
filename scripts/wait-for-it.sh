#!/bin/bash
set -e

host="localhost"
port="8000"
timeout=15
quiet=0

while [ $# -gt 0 ]
do
  case "$1" in
    --) shift; break;;
    *) shift;;
  esac
done

until curl -s "http://$host:$port/health" > /dev/null 2>&1; do
  if [ "$timeout" -le 0 ]; then
    echo "Timeout occurred after waiting for the service to start"
    exit 1
  fi
  timeout=$(($timeout - 1))
  sleep 1
done

exec "$@"
