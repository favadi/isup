#!/usr/bin/env python
import logging
import requests
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

ISUP_URL = "http://www.isup.me/"
UP_SIGN = "It's just you."


def is_up(content):
    return UP_SIGN in content


def check_status():
    exit_code = 0
    for url in sys.argv[1:]:
        try:
            response = requests.get(url=ISUP_URL+url)
            if is_up(response.content):
                logging.info('Website: %s is UP!', url)
            else:
                logging.info('Website: %s is DOWN!', url)
                exit_code = 1
        except requests.exceptions.RequestException:
            logging.error('Could\'nt connect to isup.me')
            exit_code = 1
    return exit_code

if __name__ == '__main__':
    sys.exit(check_status())
