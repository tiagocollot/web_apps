# POST /sort_names
#  Parameters:
#    names=Joe,Alice,Zoe,Julia,Kieran
#  
#  Expected response (200 OK):


def test_sorted_names(web_client):
    response = web_client.post('/sort_names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "These are the sorted names: Alice,Joe,Julia,Kieran,Zoe"


# POST /sort_names
#  Parameters: none
#  Expected response (400 Bad Request):

def test_sorted_names_400(web_client):
    response = web_client.post('/sort_names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Something went wrong"