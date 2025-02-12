# Mr. Spock Chatbot

Mr. Spock is a simple rule-based chatbot built using **Python, Streamlit, and NLTK**. It provides a conversational interface where users can chat with the bot through a web-based UI.

## 🚀 Features
- Interactive chatbot powered by **NLTK's Chat module**.
- Simple and **predefined conversation patterns (rules-based responses)**.
- **Streamlit** for a web-based UI.
- Custom **chat interface with styled messages**.
- Maintains **chat history** within the session.

## 🛠️ Installation & Setup
### 1️⃣ Install Dependencies
Make sure you have **Python 3.7+** installed. Then, install the required Python libraries:
```bash
pip install streamlit nltk
```

### 2️⃣ Run the Chatbot
Run the following command in your terminal:
```bash
streamlit run chatbot.py
```
This will open the chatbot in your web browser.

## 📜 How It Works
1. The chatbot uses **NLTK's Chat module** to define a set of **pattern-response pairs**.
2. When a user inputs a message, the bot matches it against predefined patterns and responds accordingly.
3. The chat is displayed dynamically in **Streamlit**, with messages styled for better readability.
4. The chat history is stored in **Streamlit's session state**, ensuring a continuous conversation.

## 📌 Chatbot Example Conversations
```
User: Hi
Bot: Hello

User: What's your name?
Bot: My name is Mr. Spock, but you can just call me Robot and I'm a chatbot.

User: Tell me a joke
Bot: Sure! Here's one: Why don't skeletons fight each other? Because they don’t have the guts! 😄
```

## 🎨 UI Customization
The chatbot includes **custom HTML and CSS styling** to create a visually appealing chat interface. You can modify the `st.markdown()` section to adjust styling.

## 🛠 Future Improvements
- Add **Machine Learning-based responses** using **Transformer models (e.g., GPT-3, BERT)**.
- Integrate with a **database** to store and analyze conversations.
- Implement **voice-based interaction**.

## 🤝 Contributing
Feel free to fork this project and improve it! PRs are welcome. 😊

## 📜 License
This project is **open-source** and available under the **MIT License**.

---
Developed by **Sumit** using Python & Streamlit 🚀

