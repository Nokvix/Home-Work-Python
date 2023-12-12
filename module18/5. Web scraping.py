import requests
import re

response = requests.get("http://www.columbia.edu/~fdc/sample.html").text
result = re.findall(r'<h3.*>(.*)</h3>', response)
print(result)
