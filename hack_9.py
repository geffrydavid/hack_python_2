"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    longest_key = max(s, key=lambda k: len(s[k]))
    
    new_key = longest_key.capitalize()
    new_value = s[longest_key].capitalize()
    
    return {new_key: new_value}

print(fn_hack_9({"foo": "fookziman", "bar": "barziman"}))
