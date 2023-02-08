"""

This script uses the concurrent.futures library to create a ThreadPoolExecutor 
with a maximum of 5 workers. Then, it submits 5 tasks to the executor to 
concurrently call the Flask endpoint located at http://127.0.0.1:3000/

"""

import concurrent.futures
import requests


def call_flask_endpoint():
    response = requests.get("http://127.0.0.1:3000/")
    print(response.text)


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(call_flask_endpoint)
