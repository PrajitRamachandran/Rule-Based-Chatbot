import re
from rapidfuzz import fuzz
from chatbot import responses as long
from chatbot.memory import save_message

def clean_input(user_input):
    return re.split(r'\s+|[,;?!.-]\s*', user_input.lower())

def similarity(a, b):
    return fuzz.ratio(a, b)

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = sum(1 for word in user_message if word in recognised_words)

    if len(recognised_words) == 0:
        return 0

    percentage = float(message_certainty) / float(len(recognised_words))
    has_required_words = all(word in user_message for word in required_words)

    if has_required_words or single_response:
        return int(percentage * 100)
    return 0

def check_all_messages(message, raw_input):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words
        )

    # --- 1. Greetings & Casual Chat (fuzzy boost for typos) ---
    if similarity(raw_input.lower(), "hello") > 70 or similarity(raw_input.lower(), "hi") > 80:
        return long.random_greeting()

    response('See you later 👋', ['bye', 'goodbye', 'cya', 'see', 'ya'], True)
    response("I'm doing great 😎 What about you?", ['how', 'are', 'you', 'doing'], required_words=['how'])
    response("Anytime 😌", ['thanks', 'thank', 'appreciate'], True)
    response("I'm doing good too! Let's chat.", ['i', 'am', 'good', 'fine', 'great', 'okay'], required_words=['good','fine','great','okay'])
    response("That's awesome! Tell me more.", ['cool', 'awesome', 'nice', 'great', 'wow'], True)
    response("Yes, absolutely!", ['yes', 'yeah', 'yep', 'sure', 'definitely'], True)
    response("Oh, okay. No worries!", ['no', 'nope', 'nah'], True)

    # --- 2. Identity & Capabilities ---
    response(long.R_NAME, ['what', 'is', 'your', 'name', 'who', 'are', 'you'], required_words=['name'])
    response(long.R_NAME, ['who', 'are', 'you'], required_words=['who', 'you'])
    response(long.R_CREATOR, ['who', 'made', 'created', 'built', 'you', 'creator'], required_words=['made'])
    response(long.R_CREATOR, ['who', 'made', 'created', 'built', 'you', 'creator'], required_words=['built'])
    response(long.R_CAPABILITIES, ['what', 'can', 'you', 'do', 'features', 'help'], required_words=['can', 'do'])
    response(long.R_CAPABILITIES, ['help', 'me'], required_words=['help'])

    # --- 3. Interests, Tech & Hobbies ---
    response(long.R_GAMES, ['do', 'you', 'play', 'games', 'gaming', 'cod', 'codm'], required_words=['games'])
    response(long.R_GAMES, ['do', 'you', 'play', 'games', 'gaming', 'cod', 'codm'], required_words=['play'])
    response(long.R_TECH, ['tech', 'programming', 'code', 'coding', 'web', 'ai', 'development'], required_words=['code'])
    response(long.R_TECH, ['tech', 'programming', 'code', 'coding', 'web', 'ai', 'development'], required_words=['tech'])

    # --- 4. Long / Specific Responses ---
    response(long.R_ADVICE, ['give', 'me', 'advice', 'help', 'suggest'], required_words=['advice'])
    response(long.R_POEM, ['tell', 'me', 'a', 'poem'], required_words=['poem'])
    response(long.R_EATING, ['what', 'do', 'you', 'eat', 'food', 'hungry'], required_words=['eat'])
    response(long.R_WEATHER, ['what', 'is', 'the', 'weather', 'like', 'outside'], required_words=['weather'])
    
    # --- 5. Dynamic Functions ---
    response(long.random_joke(), ['tell', 'me', 'a', 'joke', 'funny', 'laugh'], required_words=['joke'])

    # Find the best match
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # If the confidence is too low, return a random unknown response
    if highest_prob_list[best_match] < 1:
        return long.unknown()

    return best_match

def get_response(user_input):
    message = clean_input(user_input)
    response = check_all_messages(message, user_input)

    save_message(user_input, response)

    return response