def test_show_balance(client):
    response = client.get('/balance')
    assert response.status_code == 200
    assert b'Your balance' in response.data

def test_deposit(client):
    response = client.post('/deposit', data={'amount': 100})
    assert response.status_code == 200
    assert b'Successfully deposited' in response.data

def test_withdraw(client):
    response = client.post('/withdraw', data={'amount': 50})
    assert response.status_code == 200
    assert b'Successfully withdrew' in response.data

def test_invalid_deposit(client):
    response = client.post('/deposit', data={'amount': -50})
    assert response.status_code == 400
    assert b'Invalid amount' in response.data

def test_invalid_withdraw(client):
    response = client.post('/withdraw', data={'amount': 200})
    assert response.status_code == 400
    assert b'Insufficient funds' in response.data