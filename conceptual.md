### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python depends on indents for code blocks and proper syntax, where JS uses curly braces.
Python has integers and floats, where JS does not differeniate between them (floating point variables only).
Python runs on servers, but not in the browser (JS does run in a browser). It is particularly used for data science, machine learning and making servers. You can run Python in the terminal console, and use dir() (Show me the methods and attributes of this object) or help() (show me help about how to use the object).
Python has specific versions. There is a particularly big difference between version 2.x and 3.x in Python, they are not compatible.
In Python, these things are falsy: 0, 0.0, "", None, False, [] (empty list), {} (empty dictionary), set() (empty set). However, in JS, [] and {} are truthy.
Python raises an exception if there are too few or too many arguments passed, where JS will not raise an exception and will call the missing arguments undefined.
Python has built in hashtables, called dictionaries and sets. JS does not have built in hashtables.
Python uses a class-based inheritance model, while JS uses prototypal inheritance. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.
  dictionary["c"] = 3
  dictionary.get("c", 3)

- What is a unit test?
A unit test is a module in Python that allows us to write code to check the functionality of our Python code. It uses classes and it is found in the Python standard library. Unit tests will test one "unit" of functionality (such as one function or method), in isolated, small pieces. It also allows us to see if our source code could be broken down by avoiding intermixed concerns.

- What is an integration test?
An integration tests combines units and tests them to see how they work as a whole. It answers the question, do the parts work together? 

- What is the role of web application framework, like Flask?
A web application is listening for HTTP requests from a browser, and then issues a response. The client (your browser) requests data from a web application that resides on a physical machine. The web application in turn responds to the request with the data your browser requested.
A web application framework gives us this functionality that would take a considerable amount of time to implement on our own. In general, it can be opinionated, which means it is stricter in how it can be used, or unopinionated, which means it is lightweight and flexible to use. 
Web applications can:
	- handle web requests
	- produce dynamic HTML
	- handle forms
	- handle cookies
	- connect to databases
	- provide user log-in/log-out
	- cache pages for performance

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  A URL parameter is predominately for the "subject of a page", while a query param (also called a query string) is extra information about the page, and often used when coming from a form. An example could be 'comments?sort=top'.

- How do you collect data from a URL placeholder parameter using Flask?
USERS = {
	"George": "cat",
	"Max": "dog"
}
@app.route('/user/<username>')
def show_user_profile(username):
	name = USERS[username] #(or name = USER.get(username, "Blank"))
	return f"<h1> Profile for {name}</h1>"

- How do you collect data from the query string using Flask?
if the url is: /search?term=blankets

@app.route('/search'):
def search():
	term = request.args["term"]
	return f"<h1>Search for {term}</h1>"

- How do you collect data from the body of the request using Flask?
Use the "name" attribute on the form to access the data being sent

@app.route("/add-comment", methods="POST")
def add_comment():
	comment = request.form["comment"]

	#Save to database

	return f"<h1>Here is your {comment}</h1>"

- What is a cookie and what kinds of things are they commonly used for?
A cookie is name/value pair stored by the client (browser). The server tells the client to store these. The client sends cookies to the server with each request. It is a constant back and forth dialogue between the client and the server. They are commonly used to save data on your activities on the website. For example, Amazon would save what items you have looked at, what you have added to your cart, what denomination the prices should be shown in, etc. 

- What is the session object in Flask?
Session are Flask's improvements on cookies, since cookies are only strings, they're limited to a small size, and generally low-level. Sessions function like a dictionary. They contain the info for the current browser, preserve type (lists stay lists), and they are "signed" so users cannot modify data (and they aren't human readable)

- What does Flask's `jsonify()` do?
It sends our data to the browser in JSON format.

- What was the hardest part of this past week for you?
  What was the most interesting?
The hardest part was understanding the difference between URL parameters and a URL query param (also known as a query string). Also, understanding sessions modifiying them. 

Example: 
However, for a list stored in the session, you’ll need to rebind the name in the session, like so:

fruits = session['fruits']
fruits.append("cherry")
session['fruits'] = fruits

The most interesting part was seeing how the dialogue between the server and the front end works. In my previous code, the backend part was only handled by an API, so this was the first time I saw them all work together.

Time: 2 hours for conceptual