
"""
GET /names?add=Eddie
Expected response (200 OK):
"Names list: Julia, Alice, Karim, Eddie"
"""
def test_get_list_names(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Names list: Julia, Alice, Karim, Eddie"