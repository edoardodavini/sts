import re


# fill a string with the responses available at the moment
def fill_regex(string, responses):
    results = re.findall(r"{{(.+?(?=}}))}}", string, flags=re.S)
    if results is None or len(results) == 0:
        return string
    else:
        for result in results:
            array_path = result.split('.')
            index = int(array_path[0])
            path = '.'.join(array_path[1:])
            replacing_value = navigate_dot(responses=responses[index], path=path)
            string = string.replace('{{' + result + '}}', str(replacing_value))

        return string


# nested navigation with dot notation
def navigate_dot(responses, path):
    split_path = path.split('.')
    if len(split_path) > 1:
        inner_path = '.'.join(split_path[1:])
        inner_responses = responses.get(split_path[0], None)
        if inner_responses is not None and isinstance(inner_responses, dict):
            return navigate_dot(inner_responses, inner_path)
        else:
            print('FATAL!')
            return 0
    else:
        return responses.get(split_path[0], None)
