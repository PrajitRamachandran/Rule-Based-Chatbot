# Rule-Based Chatbot

## Overview
This project is a rule-based chatbot web application built with Flask and vanilla JavaScript. It does not use a machine learning model. Instead, it responds through predefined conversational rules, keyword scoring, fuzzy greeting detection, random response selection, and simple in-memory chat history storage.

## Tech Stack
- Python
- Flask
- RapidFuzz for fuzzy text similarity
- Python `re` for input tokenization
- Python `random` for dynamic greetings, jokes, and fallback messages
- HTML, CSS, and vanilla JavaScript
- Google Fonts
- Font Awesome via CDN

## Tools And Logic Components Used
- Rule-based intent matching
- Keyword overlap scoring
- Required-word validation
- Fuzzy greeting detection with `rapidfuzz.fuzz.ratio`
- In-memory conversation history using a Python list
- Fetch API for async frontend-to-backend chat requests

## Core Logic
### 1. Frontend message flow
The browser sends the user message to `/chat` as JSON using `fetch()`. The UI immediately renders the user message and shows a temporary `Processing...` state until the backend reply arrives.

### 2. Input cleaning
`clean_input()` converts the input to lowercase and splits it into tokens using whitespace and punctuation. This gives the chatbot a normalized word list for rule matching.

### 3. Fuzzy greeting detection
Before regular rule scoring runs, the bot checks whether the raw input is close to `"hello"` or `"hi"` using RapidFuzz. This helps it handle small spelling mistakes in simple greetings.

### 4. Rule scoring
The chatbot uses `message_probability()` to score a response based on:
- how many recognized words appear in the cleaned message
- whether certain required words are present
- whether the response is marked as a single-response shortcut

Each candidate response is assigned a score, and the highest-scoring reply is chosen.

### 5. Response sources
The bot combines:
- fixed responses such as identity, creator, capabilities, weather, and advice
- random greetings
- random joke responses
- random fallback responses for unknown input

### 6. Memory
After every exchange, the chatbot stores the user message and bot reply in an in-memory list through `save_message()`. The `/history` route returns that history as JSON.

## Project Structure
```text
Rule Based Chatbot/
  README.md
  app.py
  chatbot/
    logic.py
    memory.py
    responses.py
  static/
    script.js
    style.css
  templates/
    index.html
```

## Important Files
- `app.py`: Flask routes for the main page, `/chat`, and `/history`
- `chatbot/logic.py`: tokenization, similarity checks, scoring, and response selection
- `chatbot/responses.py`: static responses and random-response helpers
- `chatbot/memory.py`: in-memory chat-history store
- `static/script.js`: frontend message rendering and async API calls
- `static/style.css`: chat UI styling and animations
- `templates/index.html`: chatbot layout

## How To Run
```bash
cd "Rule Based Chatbot"
pip install flask rapidfuzz
python app.py
```

Then open `http://127.0.0.1:5000`.

## Current Behavior Notes
- Chat history is stored only in memory, so it is lost whenever the app restarts.
- The chatbot is deterministic in structure but partly dynamic because some replies are randomly chosen.
- This is a classic rule-based NLP project, so it works best for the intents and keywords explicitly coded in `logic.py`.
- The `/history` endpoint exposes prior messages as JSON, but the current frontend only uses the live chat flow.

## Summary
This project showcases a well-structured rule-based chatbot using Flask, RapidFuzz, keyword matching, simple intent scoring, random canned responses, and a polished single-page chat interface.
