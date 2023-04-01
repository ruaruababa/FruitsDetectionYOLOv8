import json
import logging
import os
import urllib
from typing import Union

import pandas as pd
import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError

logging.basicConfig(filename="log.json", level=logging.INFO, format="%(message)s")


def call_request(url) -> Union[HTTPError, dict]:
    user_agent = UserAgent()
    headers = headers = {"User-Agent": str(user_agent)}
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e

    return response.json()


if __name__ == "__main__":
    fruits = [
        "apple",
        "banana",
        "orange",
        "kiwi",
        "strawberry",
        "blueberry",
        "mango",
        "pineapple",
        "watermelon",
        "grape",
        "pear",
        "peach",
        "mango",
        "cherry",
        "lemon",
        "lime",
        "grapefruit",
        "avocado",
        "melon",
    ]
    per_page = 30
    page = 1
    path = r"C:\Users\admin\Desktop"
    image_folder_path = path + "\Images"
    image_list = []
    response_list = []

    if not os.path.isdir(image_folder_path):
        os.mkdir(image_folder_path)
    # find all page images with keyword
    for i in range(len(fruits)):
        genre = fruits[i]
        # parameter = {"query": genre, "per_page": per_page, "page": page}
        # query = urllib.parse.urlencode(parameter)
        # url = f"https://unsplash.com/napi/search/photos?{query}"
        # response = call_request(url)
        for j in range(1, 11):
            parameter = {"query": genre, "per_page": per_page, "page": j}
            query = urllib.parse.urlencode(parameter)
            url = f"https://unsplash.com/napi/search/photos?{query}"
            response_ = call_request(url)
            response_list.append(response_)
            print(url)

    res_len = len(response_list)
    fruits_len = len(fruits)
    range_list = res_len / fruits_len
    for i in range(len(fruits)):
        genre = fruits[i]
        for m in range(round(range_list)):
            rs = m * 30
            if len(response_list[m]["results"]) > 0:
                for n in range(len(response_list[m]["results"])):
                    index = n + 1
                    print(response_list[n]["results"][n]["id"])
                    filename = f"{genre}_{index + rs}.jpg"
                    folder_path = os.path.join(image_folder_path, genre)
                    if not os.path.isdir(folder_path):
                        os.mkdir(folder_path)
                    filepath = os.path.join(folder_path, filename)
                    r = requests.get(
                        response_list[n]["results"][n]["urls"]["raw"],
                        allow_redirects=True,
                    )
                    open(filepath.replace("\\", "/"), "wb").write(r.content)
