import streamlit as st
from nltk.chat.util import Chat, reflections


#Defining pairs of the chatbot
pairs = [
    [r"(.*)my name is(.*)",["Hello %2, How are you today ?",]],
    [r"(.*)help(.*)",["I can help you ",]],
    [r"(.*) your name ?", ["My name is Mr. Spock, but you can just call me robot and I'm a chatbot .",]],
    [r"how are you (.*) ?", ["I'm doing very well", "I am great !"]],
    [r"sorry (.*)", ["It's alright", "It's OK, never mind that",]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that", "Alright, great !",]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello", "Hey there",]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse",]],
    [r"(.*)created(.*)", ["Sumit created me using Python's NLTK library", "Top secret 🤫",]],
    [r"(.*) (location|city) ?", ["Hyderabad, India",]],
    [r"(.*)raining in (.*)", ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain",]],
    [r"how (.*) health (.*)", ["Health is very important, but I am a Robot, so I don't need to worry about my health ",]],
    [r"(.*)(sports|game|sport)(.*)", ["I'm a very big fan of Cricket",]],
    [r"who (.*) (Cricketer|Batsman)?", ["Virat Kohli"]],
    [r"(.*)joke|Joke(.*)",["Sure! Here's one: Why don't skeletons fight each other? Because they don’t have the guts! 😄",]],
    [r"(.*)Crazy|crazy(.*)",["My developer is ... so am I !💀",]],
    [r"quit", ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]],
    [r"(.*)", ['Our customer service will reach you']]
]


# Inject custom HTML and CSS for styling
st.markdown(
    """
    <style>
    .chat-container {
        width: 400px;
        margin: 50px auto;
        border: 1px solid #dcdcdc;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .chat-header {
        background-color: #007bff;
        color: white;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }
    .chat-messages {
        padding: 15px;
        max-height: 300px;
        overflow-y: auto;
    }
    .user-message {
        text-align: right;
        color: white;
        background-color: #007bff;
        padding: 8px 12px;
        margin: 5px 0;
        border-radius: 15px;
        display: inline-block;
        max-width: 80%;
    }
    .bot-message {
        text-align: left;
        color: black;
        background-color: #f1f1f1;
        padding: 8px 12px;
        margin: 5px 0;
        border-radius: 15px;
        display: inline-block;
        max-width: 80%;
    }
    .input-container {
        display: flex;
        padding: 10px;
        border-top: 1px solid #dcdcdc;
    }
    .chat-input {
        flex: 1;
        padding: 10px;
        border: 1px solid #dcdcdc;
        border-radius: 5px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



#frontend
st.title("🤖Chatbot: Mr. Spock")
# create chatbot object
chat = Chat(pairs, reflections)
def get_response(user_input):
    return chat.respond(user_input)
#session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#display chat history

st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{message}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input and Bot response
user_input = st.text_input("Type your message here...")

if user_input:
    
    # Append user message
    st.session_state.chat_history.append(("You", user_input))

    # Generate bot response (replace this with your chatbot logic)
    response = chat.respond(user_input)
    if response:
        st.session_state.chat_history.append(("Mr.Spock",response))
    else:
        st.session_state.chat_history.append(("Mr.Spock", "Our Costumer will reach you"))
chat.converse()
