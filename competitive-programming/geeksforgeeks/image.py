import re

url = """<div> My profile <img width="300" height="300" src="http://domain.com/profile.jpg"> </div>"""

link = re.compile("""src=[\"\'](.+)[\"\']""")

links = link.finditer(url)
for l in links:
    print(l.group())
