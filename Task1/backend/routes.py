from flask import Blueprint, request, jsonify
from models import db, Task, Comment

routes = Blueprint('routes', __name__)

# Create a comment
@routes.route("/tasks/<int:task_id>/comments", methods=["POST"])
def add_comment(task_id):
    data = request.get_json()
    comment = Comment(content=data['content'], task_id=task_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({"message": "Comment added"}), 201

# Read all comments for a task
@routes.route("/tasks/<int:task_id>/comments", methods=["GET"])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([{"id": c.id, "content": c.content} for c in comments])

# Update a comment
@routes.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    data = request.get_json()
    comment = Comment.query.get_or_404(comment_id)
    comment.content = data['content']
    db.session.commit()
    return jsonify({"message": "Comment updated"})

# Delete a comment
@routes.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"})
