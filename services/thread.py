import threading

from crawl_image import start_crawl

shared_resource = 0
lock = threading.Lock()


if __name__ == "__main__":
    fruits = [
        "dragon fruit",
        "papaya",
        "durian",
        "apple",
        "banana",
        "orange",
        "pineapple",
        "watermelon",
        "mango",
        "avocado",
    ]
    my_threads = []
    for i in range(len(fruits)):
        t = threading.Thread(target=start_crawl, args=(fruits[i],))
        my_threads.append(t)
        t.start()

    for t in my_threads:
        t.join()
