from http import HTTPStatus

def test_make_short_answer_request(client):
    data = {
        "query": "Who is PM of india?",
        "units":"imperial"
    }
    url = "/shortanswer"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_make_short_answer_request_fail(client):
    data = {
        "query":"",
    }
    url = "/shortanswer"
    response = client.post(url, json=data)
    response = response.data.decode("utf-8")
    assert response == '{"success": true, "answer": "Wolfram|Alpha did not understand your input"}'

def test_make_short_answer_request(client):
    data = {
        "query": "",
        "units":"imperial"
    }
    url = "/shortanswer"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK