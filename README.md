# 📝 Task & Comment Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg?logo=react)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000.svg?logo=flask)](https://flask.palletsprojects.com/)

> A full-stack CRUD application for managing tasks and their associated comments, built with Flask and React.

## ✨ Features

- 🔨 **Full CRUD Operations** - Create, read, update, and delete comments
- 🗃️ **Task-Comment Relationship** - Comments are linked to specific tasks
- ⚡ **RESTful API** - Well-structured Flask backend with clear endpoints
- 🧪 **Comprehensive Testing** - Backend APIs tested with Pytest
- 💅 **Modern UI** - Beautiful React interface styled with Tailwind CSS
- 🔄 **Real-time Updates** - Instant UI updates after operations
- 📱 **Responsive Design** - Works seamlessly on all device sizes

## 🔧 Tech Stack

### Backend
- **Python 3.7+**
- **Flask** - Web framework
- **SQLite** - Database
- **Flask-CORS** - Cross-origin resource sharing
- **Pytest** - Testing framework

### Frontend
- **React 18+** - UI framework
- **Axios** - HTTP client
- **Tailwind CSS** - Styling
- **JavaScript ES6+**

## 📂 Project Structure

```
task-comment-manager/
├── backend/
│   ├── app.py              # Flask API with CRUD routes
│   ├── test_app.py         # Unit tests for APIs
│   ├── requirements.txt    # Python dependencies
│   └── database.db         # SQLite database (auto-generated)
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── index.js        # React entry point
│   │   └── index.css       # Tailwind imports
│   ├── package.json        # Node.js dependencies
│   └── tailwind.config.js  # Tailwind configuration
│
├── README.md
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Node.js 14.0 or higher
- npm or yarn

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/task-comment-manager.git
   cd task-comment-manager
   ```

2. **Navigate to backend directory**
   ```bash
   cd backend
   ```

3. **Create and activate virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask application**
   ```bash
   python app.py
   ```
   
   The backend server will start at `http://localhost:5000`

### Frontend Setup

1. **Open a new terminal and navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**
   ```bash
   npm install
   ```

3. **Start the React development server**
   ```bash
   npm start
   ```
   
   The frontend will open at `http://localhost:3000`

## 🧪 Running Tests

### Backend Tests
```bash
cd backend
pytest test_app.py -v
```

### Frontend Tests (if implemented)
```bash
cd frontend
npm test
```

## 📡 API Documentation

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `GET` | `/tasks/<task_id>/comments` | Retrieve all comments for a task | - |
| `POST` | `/tasks/<task_id>/comments` | Create a new comment for a task | `{"content": "comment text", "author": "author name"}` |
| `PUT` | `/comments/<comment_id>` | Update an existing comment | `{"content": "updated text", "author": "author name"}` |
| `DELETE` | `/comments/<comment_id>` | Delete a specific comment | - |

### Example API Calls

```bash
# Get all comments for task 1
curl http://localhost:5000/tasks/1/comments

# Create a new comment
curl -X POST http://localhost:5000/tasks/1/comments \
  -H "Content-Type: application/json" \
  -d '{"content": "Great task!", "author": "John Doe"}'

# Update a comment
curl -X PUT http://localhost:5000/comments/1 \
  -H "Content-Type: application/json" \
  -d '{"content": "Updated comment", "author": "John Doe"}'

# Delete a comment
curl -X DELETE http://localhost:5000/comments/1
```

## 📋 Usage

1. **Start both servers** (backend on port 5000, frontend on port 3000)
2. **Open your browser** to `http://localhost:3000`
3. **Select a task** from the dropdown or create a new one
4. **Add comments** using the comment form
5. **Edit or delete** existing comments using the action buttons

## 🛠️ Development

### Adding New Features

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests to ensure everything passes
6. Commit your changes: `git commit -am 'Add new feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

### Code Style

- **Python**: Follow PEP 8 guidelines
- **JavaScript**: Use ES6+ features and consistent formatting
- **React**: Use functional components with hooks

## 🐛 Troubleshooting

### Common Issues

**CORS Errors**
- Ensure Flask-CORS is installed and configured
- Check that the backend server is running on port 5000

**Database Issues**
- The SQLite database is created automatically
- Delete `database.db` to reset the database

**Port Conflicts**
- Backend runs on port 5000, frontend on port 3000
- Change ports in the respective configuration files if needed

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- All contributors who helped with this project

## 📈 Roadmap

- [ ] Add user authentication
- [ ] Implement real-time updates with WebSocket
- [ ] Add comment threading/replies
- [ ] Implement comment voting system
- [ ] Add task categories and filtering
- [ ] Deploy to cloud platforms

---

⭐ **Star this repository** if you found it helpful!
