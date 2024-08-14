def validate_json(dictionary: dict, max_depth: int) -> bool:
    counter = 0

    # There are 2 options:
    # 1. There are a key and a value: key:value
    # 2. There is a key, but the value is a dictionary: key:{..}
    def count_depth(initial_key, dictionary, counter):
        for key in dictionary.keys():
            value = dictionary[key]
            counter += 1
            if isinstance(value, list):
                continue
            else:
                return count_depth(initial_key, value, counter)

        if counter <= max_depth:
            return True
        return False

    return count_depth("", dictionary, counter)
