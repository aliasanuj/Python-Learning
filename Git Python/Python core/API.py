#Application programming interface
===================================
#Application Programming Interface :
======================================
#Application Program Interfaces, or APIs, are commonly used to retrieve
#data from remote websites. Sites like Reddit, Twitter, and Facebook all offer 
#certain data through their APIs. To use an API, you make a request to a remote web 
#server, and retrieve the data you need.

#But why use an API instead of a static dataset you can download? APIs are useful in the following cases:
#1.The data is changing quickly. An example of this is stock price data. 
#It doesn't really make sense to regenerate a dataset and download it every minute -- 
#this will take a lot of bandwidth, and be pretty slow.
#2.You want a small piece of a much larger set of data. Reddit comments are one example.
# What if you want to just pull your own comments on Reddit? It doesn't make much sense
# to download the entire Reddit database, then filter just your own comments.
#3.There is repeated computation involved. Spotify has an API that can tell you 
#the genre of a piece of music. You could theoretically create your own classifier,
# and use it to categorize music, but you'll never have as much data as Spotify does.

#API Requests :- 
#1.APIs are hosted on web servers. When you type www.google.com in your browser's address bar, 
#your computer is actually asking the www.google.com server for a webpage, which it then returns to your browser.
#2.APIs work much the same way, except instead of your web browser asking for a webpage, 
#your program asks for data. This data is usually returned in JSON format 
#(for more on this, checkout our tutorial on working with JSON data).
#3.In order to get the data, we make a request to a webserver. 
#The server then replies with our data. In Python, we'll use the requests library to do this.
#In this Python API tutorial we'll be using Python 3.4 for all of our examples.


#Type of requests : 
#There are many different types of requests. 
#The most commonly used one, a GET request, is used to retrieve data.
#We can use a simple GET request to retrieve information from the OpenNotify API.

#Python Request Libarary : 
#1.The Requests library for Python is one of the most downloaded Python packages of 
#all time and probably one of my favourite libraries. It's one of those packages that
#abstracts so much away from what's actually happening underneath that you'll almost be 
#fooled into thinking you're the one doing all the hard work.
#2.You can use Requests to send human-readable HTTP/1.1 requests without the need 
#for loads of configuration beforehand. Here's an example of just how simple it is to use:

import requests
r = requests.get('https://api.github.com', auth=('user', 'pass'))
print(r.status_code)  # 200
print(r.headers['content-type'])  # 'application/json'


#Types of HTTP methods :
#Before we move on to making our own requests, lets quickly make sure we're all on the same page.
#There are four common HTTP methods that you are likely to use on a regular basis. These are:
1.GET - retrieves information from the chosen source.
2.POST - sends new information to the chosen source.
3.PUT - updates existing information of the chosen source.
4.DELETE - removes existing information from the chosen source

#1.Most of the time you will probably find yourself using GET requests because you'll 
#just be asking for information from the database of a specific source, like the titles 
#of every film released in 2017 from a well-known internet movie database.
#2.You are more likely to use PUSH, PUT and DELETE requests for APIs where 
#you own an account, such as Twitter or Github. These APIs will allow you to 
#send requests to add or delete tweets/repositories using your account credentials.


#The structure of a HTTP request :
#As well as the four HTTP methods, it's important to understand the anatomy 
#of the HTTP request itself. There are three key parts of a HTTP request:

#1.The request line - this part contains the request method (i.e. GET, POST, etc) 
#and the URL of the resource the request is searching for.
#2.The header - this part sends additional information to the chosen source, such as 
#the type of encoding (e.g. UTF-8) and the desired content type (e.g. 'application/json').
#3.The body - this part is optional, but when using the POST or PUT methods the data 
#required for the update is contained here.


>>> r = requests.get('http://swapi.co/api/planets/1/')
#The first thing to confirm is whether the request was successful, 
#which you can do by checking the status_code of the response:
>>> r.status_code
200
#A status code of 200 is the standard response of a successful HTTP request. 
#If you get a code other than 200 and you aren't getting the response from the API 
#you were expecting, it's worth finding out what the status code means to help you 
#figure out what you need to do to fix your request. 

https://en.wikipedia.org/wiki/List_of_HTTP_status_codes #--> status codes 
https://letscodepython.com/blog/2017/10/11/apis-and-python-requests-library/ #api docs

#Headers :
#Our HTTP request was successful, so we can now look at what the API sent back to us.
#You can view the response headers using .headers:

>>> r.headers
{'Via': '1.1 vegur', 'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked', 'Set-Cookie':
'__cfduid=d92acebf1060281dbc7a56a74b79e0f101494793395; expires=Mon, 14-May-18 20:23:15 GMT; 
path=/; domain=.swapi.co; HttpOnly', 'Vary': 'Accept, Cookie', 'Server': 'cloudflare-nginx', 
'Connection': 'keep-alive', 'Etag': 'W/"167b2ef894493c72d59ba5a45bab88cf"', 'Allow': 'GET, HEAD,
OPTIONS', 'Date': 'Sun, 14 May 2017 20:23:15 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Type': 
'application/json', 'CF-RAY': '35f09301b6326a37-LHR'}

#This gives us useful information like the content-type and the allowed request methods,
# which in this case are application/json and GET, HEAD, OPTIONS, respectively.


#Encoding :
#You can view the encoding of the response with .encoding, however, Swapi doesn't 
#use encoding for its responses, so to test this we are going to send a GET 
#request to httpbin.org instead:

>>> r2 = requests.get('http://httpbin.org/')
>>> r2.encoding
'utf8'

#By default the Request library will guess the encoding type of the response, 
#which will most often be utf8 and decode it accordingly, but you can change
# the encoding type yourself like the following:

>>> r2.encoding = 'ISO 8859-1'

#Contents :
#Now for the juicy bit of the response, the content.
# You can check the contents of the response using .text, or if the response 
#is in the format of JSON, the .json() method:

>>> r.text
u'{"name": "Tatooine", "rotation_period": "23", "orbital_period": "304", "diameter": 
"10465", "climate": "arid", "gravity": "1 standard", "terrain": "desert"...[remainder of response truncated]}'
>>> r.json()
{u'diameter': u'10465', u'climate': u'arid', u'surface_water': u'1', u'name': u'Tatooine',
u'created': u'2014-12-09T13:50:49.641000Z'...[remainder of response truncated]}

#The key (and possibly obvious) difference between the above is that .
#text will return the contents as a unicode string, whilst the .json() 
#method will return a JSON object. This means with the second option, 
#we can use Python dictionary notation to obtain specific content in the request:

>>> data = r.json()
>>> data['name']
u'Tatooine'

#This is useful if you are only interested in writing code that extracts certain information held by the API.

r = requests.post('https://requestb.in/15qihl81', data={'name': 'nemo'})
#Here we've used the Requests library to send a POST request using the 
#.post method, and as well as providing the URL we want to send the request to 
#we have also included some data we want the request to include.
#Just as we did for the GET request, let's test the status code of the response:
>>> r.status_code
200
#And if we check the content of the response, we should see something like this:
>>> r.text
u'ok'

#Status codes :
#The request we just made had a status code of 200. Status codes are returned with 
#every request that is made to a web server. Status codes indicate information about what 
#happened with a request. Here are some codes that are relevant to GET requests:

200 -- everything went okay, and the result has been returned (if any)
301 -- the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
401 -- the server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about authentication in a later post).
400 -- the server thinks you made a bad request. This can happen when you don't send along the right data, among other things.
403 -- the resource you're trying to access is forbidden -- you don't have the right permissions to see it.
404 -- the resource you tried to access wasn't found on the server.

#The json library has two main methods:
#1.dumps -- Takes in a Python object, and converts it to a string.
#2.loads -- Takes a JSON string, and converts it to a Python object.


