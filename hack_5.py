"""
generic script

text: "fooziman" output => "fo-zi-an" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s):
    result = ""
    for i in range(len(s)):
        # Reemplazar cada tercer carácter con un guión
        if (i + 1) % 3 == 0:
            result += '-'
        else:
            result += s[i]
    return result
