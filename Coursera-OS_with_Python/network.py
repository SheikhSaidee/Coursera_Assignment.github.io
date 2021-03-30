import requests
import socket #to check whether the local host is correctly configured or not
localhost=socket.gethostbyname('localhost')
request=requests.get("https://www.google.com/")
def check_localhost(localhost):
    if localhost=='127.0.0.1':
        return True
    else :
        return False
print(check_localhost(localhost))
def check_connectivety():
    if request.status_code ==200:
        return True
print(check_connectivety())

