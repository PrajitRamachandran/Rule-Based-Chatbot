import random

# --- Static Responses (clean + consistent) ---

R_EATING = "I run on code, not calories."

R_ADVICE = (
    "Rule-based advice is limited. If it's something important, "
    "you should double-check reliable sources."
)

R_POEM = (
    "I was over you, then I saw you again, "
    "and just like that, back to zero."
)

R_CREATOR = (
    "I was built by someone who knows AI and web development pretty well."
)

R_NAME = (
    "I'm NexaBot, a rule-based chatbot designed to simulate conversation."
)

R_CAPABILITIES = (
    "I can chat, respond to keywords, and handle simple conversations. "
    "You can ask me for jokes, tech topics, or general chat."
)

R_WEATHER = (
    "I don't have real-time weather access, but you can check a weather app for that."
)

R_GAMES = (
    "I don't play games, but I can definitely talk about them."
)

R_TECH = (
    "I can help with topics like programming, AI basics, and development concepts."
)


# --- Dynamic / Random Responses ---

def random_greeting():
    return random.choice([
        "Hey.",
        "Hello.",
        "Hi there.",
        "Hey, what's up?",
        "Hello, how can I help?"
    ])


def unknown():
    return random.choice([
        "I didn't understand that.",
        "Can you rephrase that?",
        "That didn't match any of my rules.",
        "I'm not sure what you mean.",
        "Try asking in a different way."
    ])


def random_joke():
    return random.choice([
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I would tell you a joke about UDP, but you might not get it.",
        "Why did the AI break up with the developer? It found better parameters.",
        "There are 10 types of people: those who understand binary and those who don't."
    ])