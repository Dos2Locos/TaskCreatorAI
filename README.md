# Task Event Creator 📝

A modern web application that transforms natural language task descriptions into structured JSON events using AI assistance. Built with Flask and modern JavaScript.

## ✨ Features

- 🌐 Multi-language support (English 🇬🇧, Spanish 🇪🇸, Chinese 🇨🇳)
- 🤖 AI-powered task transformation using OpenAI
- 📋 Copy-to-clipboard functionality
- 🔄 Real-time language switching
- 🐳 Docker support for easy deployment

## 🚀 Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TaskEventCreator.git
cd TaskEventCreator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key and other configurations
```

5. Run the application:
```bash
python app.py
```

### 🐳 Docker Deployment

1. Run the application with Docker Compose:

```bash
docker-compose up -d --build
```

The application will be available at `http://localhost:5000`

## 🔧 Configuration

Configure the application through environment variables in `.env`:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo  # or your preferred model
FLASK_ENV=development
```

## 📁 Project Structure

```
TaskEventCreator/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── .env.example       # Example environment variables
├── static/
│   ├── css/
│   │   └── styles.css  # Application styles
│   └── js/
│       ├── main.js     # Main application logic
│       └── i18n/       # Internationalization files
│           ├── en-GB.js
│           ├── es-ES.js
│           └── zh-CN.js
└── templates/
    └── index.html     # Main application template
```

## 🌍 Internationalization

The application supports multiple languages through a custom i18n implementation:

- 🇬🇧 English (UK)
- 🇪🇸 Spanish (Spain)
- 🇨🇳 Chinese (Simplified)

Language files are located in `static/js/i18n/` and can be easily extended to support additional languages.

## 🛠️ Development

### Adding a New Language

1. Create a new translation file in `static/js/i18n/`
2. Add translations following the existing format
3. Register the new language in `i18n.js`

### Styling

The application uses custom CSS with CSS variables for theming. Modify `static/css/styles.css` to customize the appearance.

## API Usage

The application provides an API endpoint for transforming tasks into JSON events:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"task": "Buy groceries tomorrow morning"}' \
  http://localhost:5000/transform
```

The response will contain the transformed JSON event.

```json
{
  "event": {
    "name": "Buy groceries",
    "description": "Buy groceries tomorrow morning",
    "date": "2023-08-25T10:00:00",
    "assigned_to": "John Doe",
    "emoji_icon": "🛒"
  }
}
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
