import threading

from crawl_image import start_crawl

shared_resource = 0
lock = threading.Lock()


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
    my_threads = []
    for i in range(len(fruits)):
        t = threading.Thread(target=start_crawl, args=(fruits[i],))
        my_threads.append(t)
        t.start()

    for t in my_threads:
        t.join()
