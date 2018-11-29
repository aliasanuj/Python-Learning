There are further types of Web APIs such as 
Simple Object Access Protocol (SOAP)
Remote Procedure Call (RPC)
Representational State Transfer (REST)

REST, or Representational State Transfer, is a commonly used API category that is not dependent on 
a specific protocol. It offers a flexible integration option that allows developers to use a standardized
set of processes to achieve their goals. The architectural style is straightforward and streamlines the 
connection between the client and server. REST is considered a relatively user-friendly API to work with,
and many developers are experienced in this technology.

SOAP, or Simple Object Access Protocol, is an API that connects different platforms together through HTTP 
and XML. The structure and requirements for SOAP are more rigid than REST, and it’s defined by a specific 
protocol. Web applications have started moving away from this older API type, as it’s harder to implement 
flexible integration. However, this structure does allow for more stringent security measures and includes 
stateful operations without custom coding.

API models – Public & Private APIs: 
APIs are broadly divided into internal and external based on how they are adopted and shared in a system.
Internal APIs are exclusively meant for building internal applications to use within the company or organization 
or customize it for partners to facilitate service oriented architectures. Using private or internal APIs, 
organizations can streamline business process and integrate their internal applications across their customers 
and partners. Contrary to that, public APIs are for open sharing and accessing of information and services. This 
is like an open resource where the users can create their own unique functionality by extending the original source.
Partner API model is another type where businesses work together in a strategic partnership to share data or a service.
In this case, businesses that offer API service allow third party partners to embed the service or data into their 
applications. 



Action	HTTP Verb	Description
------------------------------------
Create	POST	Create a new, unique thing
Read	GET		Read the information about a thing or collection of things
Update	PUT		Update the information about an existing thing
Delete	DELETE	Delete a thing

http://127.0.0.1:5002/employees shows ids of all the employees in database 
http://127.0.0.1:5002/tracks shows tracks details
http://127.0.0.1:5002/employees/8 shows details of employee whose employeeid is 8

==>The 200 series means "success" — your request was valid, and the response is what logically follows from it.
==>The 400 series means "bad request — something was wrong with the request, so the server did not process it as 
you wanted it to. Common causes for HTTP 400-level errors are badly-formatted requests and authentication problems.
==>The 500 series means "server error" — your request may have been OK, but the server couldn't give you a good 
response right now for reasons out of your control. These should be rare, but you need to be aware of the 
possibility so you can handle them in your code.

The Structure of HTTP / RESTful API
==>URL ( Universal Resource Locator )
==>Message Type
==>Headers
==>Parameters
==>Payload
==>Authentication

================
URL:
================
The URL is the core of RESTful API. 
Generally the URL refers a web page, but it can also refer a service or a resource.
>>> url = 'http://graph.facebook.com/v2.3/123435'

=====================
Message Types :
=====================
HTTP supports GET/POST/PUT/DELETE message types.
GET – to retrieve resource
>>> import requests
>>> ret = requests.get(url)
>>> ret.staus_code
200

POST – to update a resource :
>>> import requests
>>> ret = requests.post(url)
>>> ret.status_code
200

PUT – to create a resource:
>>> import requests
>>> ret = requests.put(url)
>>> ret.status_code
201

DELETE – to delete a resource:
>>> import requests
>>> ret = requests.delete(url)
>>> ret.status_code
200

===================
Headers:
===================
The HTTP header generally contains information used to process the request and responses.  
The headers are colon separated key value pairs. For example “Accept: text/plain”.  The http 
request & response may be have multiple headers.  Since it is a key value pair, we can use 
Python’s dictionary data type to store these values.

Single Header & Multiple headers:
>>> head = {"Content-type": "application/json"}
>>> head= {"Accept":"applicaiton/json",
        "Content-type": "application/json"}

>>> ret = requests.get(url,headers=head)
>>> ret.status_code
200

===================
Parameters:
===================
Sometimes we may want to pass values in the URL parameters.  
For example, the URL http://www.abc.com/abc.php?name=Saravanan&designation=Technical Leader 
This URL expects the user to send the value for the keyword “name” and  “designation”.    
The below code snippet helps to you accomplish this tasks.  The “params” argument is used 
to set the value for parameters.

>>> parameters = {'name':'Saravanan',
          'designation':'Technical Leader'}
>>> head = {'Content-Type':'application/json'}
>>> ret = requests.post(url,params=parameters,header=head)
>>> ret.status_code
200

==========================
Payload :
==========================
The payload contains the data to be sent on the requests.  
In this we will see how to send a JSON object in the payload.

empObj = {'name':'Saravanan', 'title':'Architect','Org':'Cisco Systems'}

As in the previous examples, we cannot send the JSON object which is a dictionary data type in Python. 
In the above snippet we created a empObj which is a dictionary data type of Python. 
This must be converted into JSON object before send the request.
The json library in Python helps here .
>>> import json
>>> emp = json.dumps(empObj)

The json.dumps converts the dictionary object into a JSON object.

>>> import json
>>> import requests
>>>
>>> url='http://graph.facebook.com/v2.3/123123
>>> head = {'Content-type':'application/json',
             'Accept':'application/json'}
>>> payload = {'name':'Saravanan',
               'Designation':'Architect',
               'Orgnization':'Cisco Systems'}

>>> payld = json.dumps(payload)
>>> ret = requests.post(url,header=head,data=payld)
>>> ret.status_code
200

====================
Authorization :
====================
The “requests” library supports various forms of authentication, which includes Basic, 
Digest Authentication, OAuth and others.  The value for authentication can be passed using 
“auth” parameter of the requests method.

>>> 
>>> from requests.auth import HTTPBasicAuth
>>> url = 'http://www.hostmachine.com/sem/getInstances'
>>> requests.get(url, auth=HTTPBasicAuth('username','password')
200
The “auth” argument can take any function, so if you want to define your own custom authentication and pass it to “auth“.








