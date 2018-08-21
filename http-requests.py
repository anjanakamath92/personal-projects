# Get and post requests to web application

import requests

#get the response contents
payload = {'url':'http://www.edge-security.com'}
r = requests.get('http://google.com', params=payload)
#print("=================================Text===============================")
#print("\n" + r.text)
print("=============================Status code:===========================")
print("\n" + str(r.status_code))

#get the response headers
h = requests.head('http://google.com')
print('Server headers')
for header in h.headers:
	print('\t' + header + ' : ' + h.headers[header])
print('=======================================================\n')

#change the user-agent in request headers
myheaders={'user-agent':'Iphone 6'}
#rq = requests.get('http://google.com/headers',headers=myheaders)
print("====================Content====================")
print("\n" + rq.text)

#post data to web application
p = requests.post('http://google.com/post, data={'name':'packt'})
