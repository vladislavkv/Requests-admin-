import requests
import getpass

#request = requests.get('')
#print(request.text)

username = 'vladislavkv'
password = getpass.getpass('Password: ')
data = requests.get('https://api.github.com/user', auth = (username, password))
data = data.json()
print(data[0])
