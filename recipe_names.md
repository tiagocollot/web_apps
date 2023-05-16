1. Design the Route Signature
​
Include the HTTP method, the path, and any query or body parameters.
​
# EXAMPLE
---------
# Request:
GET /names?add=Eddie
​
# This route should return a list of pre-defined names, plus the name given.
​
# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
----------
​
# Waving route
GET /names?add=Eddie
​
2. Create Examples as Tests
​
Go through each route and write down one or more example responses.
​
Remember to try out different parameter values.
​
Include the status code and the response body.
​
# EXAMPLE
​
# GET /names?add=Eddie
#  Expected response (200 OK):
"""
Names list: Julia, Alice, Karim, Eddie
"""
​
3. Test-drive the Route
​
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
​
Here's an example for you to start with:
​
"""
GET /names?add=Eddie
  Expected response (200 OK):
  "Names list: Julia, Alice, Karim, Eddie"
"""
def test_get_list_names(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Names list: Julia, Alice, Karim, Eddie"