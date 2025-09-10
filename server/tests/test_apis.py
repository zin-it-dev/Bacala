from .factories import CategoryFactory

def test_categories(client):
    CategoryFactory.create_batch(5)
    response = client.get('/categories/')
    assert response.status_code == 200
    assert len(response.json) == 5