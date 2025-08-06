def test_add_comment(client):
    task = Task(title="Test Task")
    db.session.add(task)
    db.session.commit()

    response = client.post(f'/tasks/{task.id}/comments', json={"content": "Test Comment"})
    assert response.status_code == 201
    assert response.get_json()['message'] == "Comment added"
