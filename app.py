import instaloader
import json


L = instaloader.Instaloader()


username = "username"

sessionfile = f"{username}.session"

try:
    with open(sessionfile, 'rb') as file:
        L.context.load_session_from_file(file)
except FileNotFoundError:

    L.context.log("Connexion à Instagram...")
    L.interactive_login(username)
    L.context.log("Enregistrement de la session...")
    with open(sessionfile, 'wb') as file:
        L.context.save_session_to_file(file)


conversation = instaloader.structures.Conversation(L.context, 'conversation_id')
messages = conversation.get_all_messages()


filename = "messages.json"
data = []
for message in messages:
    data.append({
        'text': message.text,
        'created_at': message.created_at_isoformat(),
        'is_own_message': message.is_own_message
    })

with open(filename, 'w') as file:
    json.dump(data, file)