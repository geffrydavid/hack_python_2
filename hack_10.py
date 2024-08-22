"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    counter = 1
    result = []
    
    for item in s:
        if isinstance(item, dict):
            transformed_dict = {str(counter): str(counter + 1)}
            counter += 2
        elif isinstance(item, set):
            transformed_dict = {str(counter): str(counter + 1)}
            counter += 2
        result.append(transformed_dict)
    return result

print(fn_hack_10([{"a": "b"}, {"c", "d"}, {"e": "f"}]))

