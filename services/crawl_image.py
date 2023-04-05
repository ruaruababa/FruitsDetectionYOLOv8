import json
import logging
import os
import urllib
from typing import Union

import pandas as pd
import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError


def call_request(url) -> Union[HTTPError, dict]:
    user_agent = UserAgent()
    headers = headers = {"User-Agent": str(user_agent)}
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e

    return response.json()


def start_crawl(fruit):
    log_path = os.getcwd() + "\logs"
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    fruit_log = logging.getLogger(fruit)
    fruit_log.setLevel(logging.INFO)
    fruit_log.addHandler(logging.FileHandler(f"{log_path}\{fruit}.log", "a+"))
    path = r"C:\Users\admin\OneDrive - Thuyloi University"
    image_folder_path = path + "\Images"
    response_list = []
    per_page = 30
    if not os.path.isdir(image_folder_path):
        os.mkdir(image_folder_path)

    for j in range(1, 15):
        parameter = {"query": fruit, "per_page": per_page, "page": j}
        query = urllib.parse.urlencode(parameter)
        url = f"https://unsplash.com/napi/search/photos?{query}"
        # url = f"https://pixabay.com/api/?key=34881807-c7347ca212ee6cd6f13a3806a&q={fruit}&image_type=photo&pretty=true&page={j}&per_page=200"
        response_ = call_request(url)
        response_list.append(response_)

    for m in range(len(response_list)):
        rs = m * 30
        for i in range(len(response_list[m]["results"])):
            filename = f"{fruit}_{90 + i + rs}.jpg"
            print(f"Downloading {filename}...")
            print(f"ID: {response_list[m]['results'][i]['id']}")
            fruit_log.info(f"{m}: {response_list[m]['results'][i]['id']}")
            folder_path = os.path.join(image_folder_path, fruit)
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)
            filepath = os.path.join(folder_path, filename)
            r = requests.get(
                response_list[m]["results"][i]["urls"]["raw"], allow_redirects=True
            )
            open(filepath.replace("\\", "/"), "wb").write(r.content)

    print(f"Downloaded {fruit} images successfully!")
    # per_page = 30
    # page = 1
    # path = r"C:\Users\admin\Desktop"
    # image_folder_path = path + "\Images"
    # image_list = []
    # response_list = []

    # if not os.path.isdir(image_folder_path):
    #     os.mkdir(image_folder_path)
    # find all page images with keyword
    # for i in range(len(fruits)):
    #     genre = fruits[i]
    # parameter = {"query": genre, "per_page": per_page, "page": page}
    # query = urllib.parse.urlencode(parameter)
    # url = f"https://unsplash.com/napi/search/photos?{query}"
    # response = call_request(url)
    # for j in range(1, 11):
    #     parameter = {"query": genre, "per_page": per_page, "page": j}
    #     query = urllib.parse.urlencode(parameter)
    #     url = f"https://unsplash.com/napi/search/photos?{query}"
    #     response_ = call_request(url)
    #     response_list.append(response_)
    #     print(url)

    # res_len = len(response_list)
    # fruits_len = len(fruits)
    # range_list = res_len / fruits_len
    # for i in range(len(fruits)):
    #     genre = fruits[i]
    #     start = i + 1
    #     data = response_list[i * 10 : (start * 10)]
    #     for m in range(len(data)):
    #         rs = m * 30
    #         for i in range(len(data[m]["results"])):
    #             filename = f"{genre}_{i + rs}.jpg"
    #             folder_path = os.path.join(image_folder_path, genre)
    #             if not os.path.isdir(folder_path):
    #                 os.mkdir(folder_path)
    #             filepath = os.path.join(folder_path, filename)
    #             r = requests.get(
    #                 data[m]["results"][i]["urls"]["raw"], allow_redirects=True
    #             )
    #             open(filepath.replace("\\", "/"), "wb").write(r.content)
