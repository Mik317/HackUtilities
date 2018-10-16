import os
import webbrowser as bro

url = input("Insert the url to test: ")
el = input("ID of the element to point: ")
html = '''<html><body>
<iframe src="{}"></iframe>
</body></html>'''.format(url+'#'+el)

with open("test.html", "w") as file:
    file.write(html)
    bro.open(os.path.abspath(file.name))
    print(os.path.abspath(file.name))
