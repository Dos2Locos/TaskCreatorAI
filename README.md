# Natural Language Task Transformer

## Overview
This application transforms natural language task descriptions into structured JSON using OpenAI's GPT-3.5 Turbo model.

## Prerequisites
- Python 3.8+
- OpenAI API Key

## Setup
1. Clone the repository
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Running the Application
```
flask run
```

## How It Works
1. Enter a natural language task description in the text area
2. Click "Transform to JSON"
3. The app uses OpenAI to convert the description into a structured JSON format

## Example
**Input**: 
"Plan a birthday party for my friend next Saturday. Need to invite 10 people, book a venue, order a cake, and buy decorations."

**Output**:
```json
{
  "title": "Friend's Birthday Party",
  "deadline": "Next Saturday",
  "tasks": [
    "Invite 10 people",
    "Book a venue", 
    "Order a cake",
    "Buy decorations"
  ]
}
```

## Notes
- Requires an active internet connection
- JSON structure may vary based on input complexity
