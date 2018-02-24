import json

class MainHandler:
    def __init__(self, data):
        self.__got_all_data = []
        self.__got_data = None

        if isinstance(data, dict):
            self.data = data
        elif isinstance(data, (str, bytes)):
            self.data = json.loads(data)
        else:
            raise Exception("Unsupport %s data type!" % self.__class__.__name__)

    def get(self, key):
        self.__traversal_dict(key, self.data, all=True)
        return self.__got_data

    def get_all(self, key):
        self.__traversal_dict(key, self.data, all=False)
        return self.__got_all_data

    """traversal to search key"""

    def __traversal_dict(self, key, dictionary, all):
        if isinstance(dictionary, dict):
            for x in range(len(dictionary)):
                temp_key = list(dictionary.keys())[x]
                temp_value = dictionary[temp_key]
                if temp_key == key:
                    if all:
                        self.__got_all_data.extend(temp_value)
                    else:
                        self.__got_data = temp_value
                    return

                self.__traversal_dict(key, temp_value, all=all)
        else:
            return None
