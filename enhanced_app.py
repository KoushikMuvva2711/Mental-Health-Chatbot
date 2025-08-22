# Enhanced backend.py with data storage - preserving original functionality
import os
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# Database initialization for storing conversations and user data
def init_database():
    conn = sqlite3.connect('mental_health_chat.db')
    cursor = conn.cursor()

    # Create conversations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            response_time REAL
        )
    ''')

    # Create user_sessions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_sessions (
            session_id TEXT PRIMARY KEY,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_active DATETIME DEFAULT CURRENT_TIMESTAMP,
            total_messages INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Initialize components - PRESERVING YOUR EXACT IMPLEMENTATION
def initialize_components():
    # Document loading and processing
    loader = DirectoryLoader(
        "C:/Users/koush/Desktop/mental health/data",
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Embeddings and vector store
    embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = Chroma.from_documents(texts, embeddings, persist_directory="./chroma_db")

    # LLM and QA chain
    llm = ChatGroq(
        temperature=0,
        groq_api_key="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",
        model_name="llama-3.3-70b-versatile"
    )

    # Mental health focused prompt - YOUR EXACT PROMPT
    prompt_template = """You are a mental health specialist assistant. Follow these rules:
    1. Only answer questions about mental health, emotions, or psychological well-being
    2. If asked about other topics, respond: "I specialize in mental health. How can I help you with emotional concerns?"
    3. Use this context to help:
    {context}

    Question: {question}
    Helpful Answer:"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(),
        chain_type_kwargs={"prompt": PROMPT}
    )

# Database helper functions
def store_conversation(session_id, user_message, bot_response, response_time):
    conn = sqlite3.connect('mental_health_chat.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO conversations (session_id, user_message, bot_response, response_time)
        VALUES (?, ?, ?, ?)
    ''', (session_id, user_message, bot_response, response_time))

    cursor.execute('''
        INSERT OR REPLACE INTO user_sessions (session_id, last_active, total_messages)
        VALUES (?, CURRENT_TIMESTAMP, 
                COALESCE((SELECT total_messages FROM user_sessions WHERE session_id = ?), 0) + 1)
    ''', (session_id, session_id))

    conn.commit()
    conn.close()

def get_conversation_history(session_id, limit=10):
    conn = sqlite3.connect('mental_health_chat.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT user_message, bot_response, timestamp 
        FROM conversations 
        WHERE session_id = ? 
        ORDER BY timestamp DESC 
        LIMIT ?
    ''', (session_id, limit))

    history = cursor.fetchall()
    conn.close()
    return list(reversed(history))

# Initialize database and components
init_database()
qa_chain = initialize_components()

@app.route('/')
def index():
    return render_template('enhanced_index.html')

@app.route("/chat", methods=["POST"])
def chat():
    start_time = datetime.now()

    data = request.json
    user_input = data.get("message", "").strip()
    session_id = data.get("session_id", "default_session")

    if not user_input:
        return jsonify({"response": "Please enter a valid question"})

    try:
        # YOUR EXACT PROCESSING LOGIC - UNCHANGED
        result = qa_chain.invoke({"query": user_input})
        bot_response = result["result"]

        # Calculate response time
        response_time = (datetime.now() - start_time).total_seconds()

        # Store conversation in database
        store_conversation(session_id, user_input, bot_response, response_time)

        return jsonify({
            "response": bot_response,
            "session_id": session_id,
            "response_time": response_time
        })

    except Exception as e:
        error_response = f"Error processing request: {str(e)}"
        store_conversation(session_id, user_input, error_response, 0)
        return jsonify({"response": error_response})

@app.route("/history/<session_id>", methods=["GET"])
def get_history(session_id):
    history = get_conversation_history(session_id)
    return jsonify({"history": history})

if __name__ == "__main__":
    print("🧠 Mental Health Assistant Backend Starting...")
    print("📊 Database initialized for conversation storage")
    print("🤖 LangChain + Groq + Chroma pipeline ready")
    print("🌐 Server running on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
