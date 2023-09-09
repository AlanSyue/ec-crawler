import pchome
import momo
import eslite


class TopicFactory:
    def make(topic_name: str):
        if topic_name == "pchome":
            return pchome
        elif topic_name == "momo":
            return momo
        elif topic_name == "eslite":
            return eslite
        else:
            raise Exception("Invalid topic name")