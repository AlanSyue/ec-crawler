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
    token = os.getenv('LINE_NOTIFY_TOKEN')

    try:
        topic = TopicFactory.make(topic_name)

        for url in topic.urls():
            sleep_time = random.uniform(1, 5)
            time.sleep(sleep_time)

            response = topic.request(url)
            stock = topic.parse(response)

            if stock == 0:
                continue

            message = f"[{topic_name}] 有 {stock} 貨量，網址：{url}"
            lineTool.lineNotify(token, message)
    except Exception as e:
        message = f"[{topic_name}] error: {e}"
        lineTool.lineNotify(token, message)
        exit(1)
