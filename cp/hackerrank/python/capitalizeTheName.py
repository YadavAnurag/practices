def solve(s):
    string = ''
    for i,e in enumerate(s):
    	if(s[i-1]==' ' and s[i]!=' '):
    		string+=s[i].upper()
    	else:
    		string+=s[i]
    return s[0].upper()+string[1:]

print(solve('hello   world         lol'))