"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    
    n = len(s)
    result = []
    
    if n % 2 != 0:  
        for i in range(n):
            result.append(f"{s[-(i+1)]}-{n-i}")
    else:  
        for i in range(n):
            result.append(str(n - i))
        
    return result


print(fn_hack_8(["a", "b", "c", "d", "e"]))
print(fn_hack_8(["a", "b", "c"]))  
print(fn_hack_8(["a", "b", "c", "d"]))  
print(fn_hack_8(["a", "b"]))  

