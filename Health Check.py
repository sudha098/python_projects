import requests
import logging
import sys
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

URL = "https://example.com"
TIMEOUT = 5
RETRIES = 3
SLEEP_BETWEEN_RETRIES = 2


def check_health(url):
    for attempt in range(1, RETRIES + 1):
        try:
            response = requests.get(url, timeout=TIMEOUT)

            if response.status_code == 200:
                logging.info("Service is healthy")
                return True
            else:
                logging.warning(
                    f"Attempt {attempt}: Received status code {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {attempt} failed: {e}")

        time.sleep(SLEEP_BETWEEN_RETRIES)

    return False


if __name__ == "__main__":
    if not check_health(URL):
        logging.error("Service is DOWN")
        sys.exit(1)
