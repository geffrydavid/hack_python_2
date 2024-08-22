"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    
    if len(s) > 3:
        result = s[1:-1]
        return result
    else:
        result = s
    return result
