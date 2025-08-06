# Python Docker CI/CD with AI Code Review

This is a simple Flask application with a complete CI/CD pipeline using GitHub Actions and AI-assisted code review powered by OpenAI's GPT model.

## 🔧 Features

- ✅ Flask-based web application
- 🧪 Unit testing with `pytest`
- 🐳 Docker containerization
- ⚙️ GitHub Actions for CI/CD:
  - Automatic testing on push/PR
  - AI-powered code review with GPT (OpenAI)
- 🔐 Uses GitHub Secrets to securely pass API keys

## 📁 Project Structure

```
.
├── app/
│   └── app.py               # Flask app
├── tests/
│   └── test_app.py          # Sample test
├── scripts/
│   └── ai_review.py         # AI code reviewer using OpenAI
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow
├── Dockerfile               # Docker container setup
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/python-docker-cicd-ai.git
cd python-docker-cicd-ai
```

### 2. Run locally
```bash
pip install -r requirements.txt
python app/app.py
```

### 3. Run tests
```bash
pytest tests/
```

### 4. Build Docker image
```bash
docker build -t my-python-app .
docker run -p 5000:5000 my-python-app
```

## 🤖 GitHub Actions CI/CD Setup

This project uses GitHub Actions for:

- Installing dependencies
- Running unit tests
- Running AI code review using GPT

### Enable AI Code Review

1. Get your OpenAI API key from https://platform.openai.com/
2. On GitHub, go to:  
   `Settings → Secrets and Variables → Actions → New repository secret`
3. Add:
   - `Name`: `OPENAI_API_KEY`
   - `Value`: `your-api-key`

Now, whenever a Pull Request is opened, the AI will review your code and suggest improvements in the logs.

## 🧠 AI Review Logic

The `scripts/ai_review.py` file reads your code and submits it to GPT-4 for feedback.

---

Made with ❤️ using Python, GitHub Actions, and OpenAI.