"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    
    replacements = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
        }
    
    result = ''.join(replacements.get(c, c) for c in s)
    
    if len(result) > 1:
        result = result[0].upper() + result[1:-1] + result[-1].upper()
    else:
        result = result.upper()

    return result