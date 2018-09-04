import os
import webbrowser as bro

url = input("Insert the url to test: ")
html = '''<html><body>
<iframe src="{}">
</body></html>'''.format(url)

with open("test.html", "w") as file:
    file.write(html)
    bro.open(os.path.abspath(file.name))
