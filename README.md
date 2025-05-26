
# 🤖 WISP – AI Chatbot Using Groq API & Streamlit

WISP is a sleek and simple AI-powered chatbot that leverages the **Groq API** and **Streamlit** to provide real-time, intelligent conversations. Built as a personal project, WISP demonstrates my understanding of API integration, environment variable security, Python backend logic, and frontend development using Streamlit.

---

## 🚀 Features

- 🌐 **Web-based UI** powered by Streamlit
- 🤝 **Connects to Groq API** (LLaMA 3-70B) for smart, real-time responses
- 🔒 Uses `.env` file to **secure API keys**
- 💬 Keeps **chat history** within the session
- 🪄 Real-time typing animation for realistic interaction
- 🎨 Custom avatars and branding to personalize the chat

---

## 🧰 Tech Stack

| Layer       | Tools/Tech              |
|-------------|--------------------------|
| Frontend    | Streamlit                |
| Backend     | Python                   |
| AI Engine   | Groq API (LLaMA 3 Model) |
| Security    | python-dotenv for .env   |
| Deployment  | Streamlit Cloud (Optional) |

---

## 📸 Preview

![WISP Preview](https://raw.githubusercontent.com/CIBIRAJGL/WISP/main/Resources/preview.png)

> ✨ **Hint:** Replace the link above with your own GitHub image link OR:
> - Place your screenshot in the `Resources/` folder.
> - Name it `preview.png`.
> - Make sure it’s committed to your GitHub repo.

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/WISP.git
cd WISP
```

### 2. Set Up Your Environment

- Create a `.env` file:

```
GROQ_API_KEY=your_real_api_key_here
```

> ❗ Never push this `.env` file to GitHub.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run prompt.py
```

---

## 📁 Project Structure

```
WISP/
├── chatbot_groq.py       # API logic
├── prompt.py             # Streamlit UI
├── .env                  # API key (not tracked)
├── .gitignore
├── requirements.txt
├── README.md
└── Resources/
    ├── Logo.png
    └── User.png
```

---

## 🧠 What I Learned

- How to securely manage API keys using `.env`
- Integrating third-party AI APIs (Groq)
- Building interactive web apps with Streamlit
- Modularizing code for clarity and reusability
- Presenting personal projects with professionalism

---

## 💡 Future Enhancements

- 🔄 Add response streaming with real-time updates
- 📜 Save chat history to a file or database
- 🎤 Add voice input/output
- 🧪 Add unit tests and modular logging

---

## 🙋‍♂️ About Me

I'm a passionate mechanical engineer turned developer, diving deep into AI and software engineering. I created WISP to explore API integration and create something interactive from scratch. I'm actively looking for opportunities in software development, webdevelopment, backend engineering, or AI/ML.

📫 **Let's connect!**
- Email: cibiloganathan@email.com
- LinkedIn:(https://www.linkedin.com/in/cibirajgl)

---

## ⭐ Give it a Star!

If you like this project, show some ❤️ by starring the repository!
