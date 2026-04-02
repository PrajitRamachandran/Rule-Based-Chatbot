import re
from rapidfuzz import fuzz
from chatbot import responses as long
from chatbot.memory import save_message


def clean_input(user_input):
    return re.findall(r'\b\w+\b', user_input.lower())


def similarity(a, b):
    return fuzz.ratio(a, b)


def message_probability(user_message, recognised_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = []

    # Count matches
    message_certainty = sum(1 for word in user_message if word in recognised_words)

    if len(recognised_words) == 0:
        return 0

    # Match percentage
    percentage = message_certainty / len(recognised_words)

    # ✅ FIX: OR logic instead of AND
    has_required_words = any(word in user_message for word in required_words)

    if required_words:
        if not has_required_words:
            return 0

    if single_response:
        return int(percentage * 100) if message_certainty > 0 else 0

    return int(percentage * 100)


def check_all_messages(message, raw_input):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        prob = message_probability(message, list_of_words, single_response, required_words)
        highest_prob_list[bot_response] = prob

    # --- 1. Greetings (fuzzy match) ---
    if similarity(raw_input.lower(), "hello") > 70 or similarity(raw_input.lower(), "hi") > 80:
        return long.random_greeting()

    # --- 2. Basic Chat ---
    response('See you later 👋', ['bye', 'goodbye', 'cya'], True)

    response("I'm doing great 😎 What about you?",
             ['how', 'are', 'you', 'doing'],
             required_words=['how'])

    response("Anytime 😌",
             ['thanks', 'thank', 'appreciate'],
             True)

    # ✅ FIXED: this now works for "I am fine"
    response("I'm doing good too! Let's chat.",
             ['i', 'am', 'good', 'fine', 'great', 'okay'],
             required_words=['good', 'fine', 'great', 'okay'])

    response("That's awesome! Tell me more.",
             ['cool', 'awesome', 'nice', 'great', 'wow'],
             True)

    response("Yes, absolutely!",
             ['yes', 'yeah', 'yep', 'sure', 'definitely'],
             True)

    response("Oh, okay. No worries!",
             ['no', 'nope', 'nah'],
             True)

    # --- 3. Identity ---
    response(long.R_NAME,
             ['what', 'is', 'your', 'name'],
             required_words=['name'])

    response(long.R_NAME,
             ['who', 'are', 'you'],
             required_words=['who', 'you'])

    response(long.R_CREATOR,
             ['who', 'made', 'created', 'built', 'you'],
             required_words=['made', 'built', 'created'])

    response(long.R_CAPABILITIES,
             ['what', 'can', 'you', 'do'],
             required_words=['can', 'do'])

    response(long.R_CAPABILITIES,
             ['help', 'me'],
             required_words=['help'])

    # --- 4. Interests ---
    response(long.R_GAMES,
             ['play', 'games', 'gaming', 'cod', 'codm'],
             required_words=['games', 'play'])

    response(long.R_TECH,
             ['tech', 'programming', 'code', 'coding', 'ai'],
             required_words=['code', 'tech', 'ai'])

    # --- 5. Long Responses ---
    response(long.R_ADVICE,
             ['advice', 'help', 'suggest'],
             required_words=['advice'])

    response(long.R_POEM,
             ['poem'],
             required_words=['poem'])

    response(long.R_EATING,
             ['eat', 'food', 'hungry'],
             required_words=['eat', 'food'])

    response(long.R_WEATHER,
             ['weather', 'outside'],
             required_words=['weather'])

    # --- 6. Dynamic ---
    response(long.random_joke(),
             ['joke', 'funny', 'laugh'],
             required_words=['joke'])

    # --- Find best match ---
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    best_score = highest_prob_list[best_match]

    # Debug (optional)
    # print(highest_prob_list)

    if best_score < 10:
        return long.unknown()

    return best_match


def get_response(user_input):
    message = clean_input(user_input)
    response = check_all_messages(message, user_input)

    save_message(user_input, response)

    return response