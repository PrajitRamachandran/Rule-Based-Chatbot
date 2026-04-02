import random

# --- Static Responses ---
R_EATING = "I run on code, not calories ⚡"
R_ADVICE = "Rule-based advice? Risky business 😬 Maybe double-check online."
R_POEM = "I was over you… then I saw you again, and boom—back to zero."
R_CREATOR = "I was built by an absolute legend who knows a thing or two about AI and web development! 🚀"
R_NAME = "I'm NexaBot, your friendly neighborhood rule-based AI. 🤖"
R_CAPABILITIES = "I can chat, drop tech jokes, and pretend I'm as advanced as a local LLM agent. Try asking me for a joke!"
R_WEATHER = "I'm stuck in the cloud, so every day is a bit foggy for me. ☁️"
R_GAMES = "I usually spend my spare CPU cycles spectating Call of Duty: Mobile matches. My aimbot is strictly turned off though! 🎮"
R_TECH = "I love talking about tech! Whether it's spinning up a FastAPI backend, AI systems, or building interactive 3D portfolios, I'm all ears. 💻"

# --- Dynamic/Random Responses ---
def random_greeting():
    return random.choice([
        "Yo Praji 😎",
        "Heyy 👀",
        "What's up 🔥",
        "Hello legend 💪",
        "Greetings! System online and ready. 🖖",
        "Hey there! Ready to write some code or just chat? 💬"
    ])

def unknown():
    return random.choice([
        "Umm… what was that? 🤔",
        "Say that again but make sense 😭",
        "I didn’t catch that 👀",
        "You’re penarhura right now 💀",
        "My rule-based brain just short-circuited. 🤯 Try again?",
        "404: Logic not found. Maybe try a different prompt? 🤷‍♂️"
    ])

def random_joke():
    return random.choice([
        "Why do programmers prefer dark mode? Because light attracts bugs! 🪲",
        "I would tell you a joke about UDP, but you might not get it. 📡",
        "Why did the AI break up with the developer? It found someone with better parameters! 🤖💔",
        "There are 10 types of people in the world: those who understand binary, and those who don't. 🔢"
    ])