from controller.my_blueprints import bp

def test_home_page():
    client = bp.test_client()
    response = client.get('/footballer-pulse/')
    assert response.status_code == 200
    assert b'Welcome to the Football-Pulse!' in response.data


    