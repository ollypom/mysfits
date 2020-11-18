import json
import logging
import requests
import sys

# Logging to stout
logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

URL='http://localhost'
PORT='8080'
TIMEOUT=2000

# Health Check
response = requests.get(URL + ':' + PORT + '/', timeout=TIMEOUT)

if response.status_code == requests.codes.ok:
  logging.info('Successful healthcheck {}'.format(response.status_code))
  exit(0)
else:
  logging.info('Failed healthcheck {}'.format(response.status_code))
  exit(1)