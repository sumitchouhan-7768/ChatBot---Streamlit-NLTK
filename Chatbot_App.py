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
# Create the Chat object
chat = Chat(pairs, reflections)

# inject cuastom CSS


#frontend
st.markdown('<div class="chat-container">',unsafe_allow_html=True)
st.title("🤖Chatbot: Mr. Spock")
st.subheader("Welcome! Start chatting with the bot below.")
st.markdown("Type 'quit' to exit the chat.")

#session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#Chat input and output
user_input = st.text_input("You: ","",key="user_input")

if user_input:
    st.session_state.chat_history.append(("You",user_input))
    
    if user_input.lower() == "quit":
        bot_response = "Goodbye! It was nice chatting with you."
    else:
        bot_response = chat.respond(user_input)
        
    st.session_state.chat_history.append(("Mr.Spock",bot_response))        
    
# Display chat history
st.markdown("Chat History")
for sender, message in st.session_state.chat_history:
    if sender =="You":
        st.markdown(f"**{sender}:**{message}")
    else:
        st.markdown(f"**{sender}:**{message}",unsafe_allow_html=True)    
st.markdown("<hr>", unsafe_allow_html=True)  
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 12px;">
        This Bot is created by <b>Sumit ❤</b>
    </div>
    """, unsafe_allow_html=True
)