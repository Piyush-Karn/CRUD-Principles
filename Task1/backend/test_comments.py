import pytest
import json
from app import app, db, Comment
import uuid

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_comment(client):
    task_id = str(uuid.uuid4())
    response = client.post('/api/comments', 
        json={'task_id': task_id, 'content': 'Test comment'})
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['task_id'] == task_id
    assert data['content'] == 'Test comment'
    assert 'id' in data
    assert 'created_at' in data
    assert 'updated_at' in data

def test_create_comment_missing_fields(client):
    response = client.post('/api/comments', json={})
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'task_id and content are required'

def test_get_comment(client):
    task_id = str(uuid.uuid4())
    comment = Comment(task_id=task_id, content='Test comment')
    with app.app_context():
        db.session.add(comment)
        db.session.commit()
    
    response = client.get(f'/api/comments/{comment.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['content'] == 'Test comment'
    assert data['task_id'] == task_id

def test_get_comment_not_found(client):
    response = client.get(f'/api/comments/{str(uuid.uuid4())}')
    assert response.status_code == 404

def test_get_comments_by_task(client):
    task_id = str(uuid.uuid4())
    comment1 = Comment(task_id=task_id, content='Comment 1')
    comment2 = Comment(task_id=task_id, content='Comment 2')
    with app.app_context():
        db.session.add_all([comment1, comment2])
        db.session.commit()
    
    response = client.get(f'/api/comments/task/{task_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['task_id'] == task_id
    assert data[1]['task_id'] == task_id

def test_update_comment(client):
    task_id = str(uuid.uuid4())
    comment = Comment(task_id=task_id, content='Original comment')
    with app.app_context():
        db.session.add(comment)
        db.session.commit()
    
    response = client.put(f'/api/comments/{comment.id}', 
        json={'content': 'Updated comment'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['content'] == 'Updated comment'
    assert data['task_id'] == task_id

def test_update_comment_missing_content(client):
    task_id = str(uuid.uuid4())
    comment = Comment(task_id=task_id, content='Original comment')
    with app.app_context():
        db.session.add(comment)
        db.session.commit()
    
    response = client.put(f'/api/comments/{comment.id}', json={})
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'content is required'

def test_delete_comment(client):
    task_id = str(uuid.uuid4())
    comment = Comment(task_id=task_id, content='Test comment')
    with app.app_context():
        db.session.add(comment)
        db.session.commit()
    
    response = client.delete(f'/api/comments/{comment.id}')
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Comment deleted successfully'
    
    with app.app_context():
        assert Comment.query.get(comment.id) is None

def test_delete_comment_not_found(client):
    response = client.delete(f'/api/comments/{str(uuid.uuid4())}')
    assert response.status_code == 404