import pytest
from app import app  # Assuming the Flask app is in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_books(client):
    """Test GET request to fetch all books"""
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.json) > 0  # Assuming books are returned as a list

def test_post_book(client):
    """Test POST request to add a new book"""
    new_book = {'title': 'New Book', 'author': 'Author Name', 'year': 2024}
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    assert response.json['title'] == 'New Book'

def test_update_book(client):
    """Test PUT request to update a book"""
    updated_book = {'title': 'Updated Book'}
    response = client.put('/books/1', json=updated_book)
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Book'

def test_delete_book(client):
    """Test DELETE request to delete a book"""
    response = client.delete('/books/1')
    assert response.status_code == 204
