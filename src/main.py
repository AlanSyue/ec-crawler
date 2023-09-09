import sys
from factories.topic_factory import TopicFactory
import lineTool
from dotenv import load_dotenv
import os
import time
import random


if __name__ == "__main__":
    arguments = sys.argv

    if len(arguments) < 2:
        print("Please provide a topic name")
        exit(1)
    
    load_dotenv()
    topic_name = sys.argv[1]

    try:
        topic = TopicFactory.make(topic_name)

        for url in topic.urls():
            sleep_time = random.uniform(1, 10)
            time.sleep(sleep_time)

            response = topic.request(url)
            stock = topic.parse(response)

            if stock == 0:
                continue

            message = f"[{topic_name}] 有 {stock} 貨量，網址：{url}"
            token = os.getenv('LINE_NOTIFY_TOKEN')
            lineTool.lineNotify(token, message)
    except Exception as e:
        print(e)
        exit(1)
