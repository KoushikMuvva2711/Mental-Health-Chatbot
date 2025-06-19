# Mental Health Chatbot with AI-Powered Support

A sophisticated mental health support chatbot built with **LangChain**, **Groq API**, **ChromaDB**, and **HuggingFace embeddings**. Features a beautiful, responsive web interface with conversation storage and analytics.

## 🧠 Features

### Backend (Your Original Logic Preserved)
- **LangChain + Groq Integration**: Uses your exact `llama3-70b-8192` model configuration
- **HuggingFace BGE Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` for document processing
- **ChromaDB Vector Store**: Persistent document storage with your exact chunk settings
- **Mental Health Specialization**: Your original prompt template maintained
- **PDF Document Processing**: DirectoryLoader with your file paths preserved

### Enhanced Features (Added)
- **SQLite Database**: Conversation history and session management
- **Real-time Analytics**: Response times, message counts, session tracking
- **Session Management**: Persistent user sessions with conversation history
- **Error Handling**: Robust error handling with fallback responses

### Frontend (Beautiful & Dynamic)
- **Modern UI/UX**: Gradient backgrounds, glassmorphism effects, smooth animations
- **Responsive Design**: Mobile-first design that works on all devices
- **Real-time Features**: Typing indicators, message timestamps, connection status
- **Quick Actions**: Pre-defined mental health conversation starters
- **Crisis Resources**: Emergency contact information readily available
- **Session Statistics**: Live message counts, response times, session duration

## 🚀 Quick Setup

### Automatic Setup (Recommended)

**For Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

**For Windows:**
```cmd
setup.bat
```

### Manual Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.template .env
   # Edit .env with your settings
   ```

3. **Create Templates Directory**
   ```bash
   mkdir templates
   mv enhanced_index.html templates/
   ```

4. **Run the Application**
   ```bash
   python enhanced_app.py
   ```

## 📁 Project Structure

```
mental-health-chatbot/
├── enhanced_app.py              # Enhanced backend (your logic preserved)
├── templates/
│   └── enhanced_index.html      # Beautiful frontend
├── requirements.txt             # Python dependencies
├── .env.template               # Environment configuration template
├── .env                        # Your environment settings (create from template)
├── setup.sh                    # Linux/macOS setup script
├── setup.bat                   # Windows setup script
├── data/                       # Your PDF documents directory
├── chroma_db/                  # Vector database (auto-created)
├── mental_health_chat.db       # SQLite database (auto-created)
└── README.md                   # This file
```

## ⚙️ Configuration

### Environment Variables (.env)
```bash
# Your API Configuration
GROQ_API_KEY=your_groq_api_key_here
DOCS_DIRECTORY=/path/to/your/pdf/documents

# Database Settings
DATABASE_PATH=mental_health_chat.db
CHROMA_PERSIST_DIR=./chroma_db

# Model Configuration (Your Settings Preserved)
MODEL_NAME=llama3-70b-8192
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
CHUNK_SIZE=500
CHUNK_OVERLAP=50
TEMPERATURE=0
```

## 🔧 Your Original Components Preserved

✅ **Exact LangChain Pipeline**: Your RetrievalQA chain with identical configuration  
✅ **Same Groq Model**: `llama3-70b-8192` with temperature=0  
✅ **Identical Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`  
✅ **Same Chunking**: 500 chunk size, 50 overlap  
✅ **Your Prompt Template**: Mental health specialization maintained  
✅ **Same File Processing**: DirectoryLoader with PyPDFLoader  
✅ **Identical Response Logic**: Your error handling and response format  

## 🌐 Usage

1. **Start the Backend**:
   ```bash
   python enhanced_app.py
   ```

2. **Open Your Browser**:
   Navigate to `http://localhost:5000`

3. **Start Chatting**:
   - Use quick action buttons for common queries
   - Type custom mental health questions
   - View real-time response analytics
   - Access conversation history

## 📊 New API Endpoints

While preserving your original `/chat` endpoint:

- `GET /` - Serves the beautiful frontend
- `POST /chat` - Your original chat logic (enhanced with storage)
- `GET /history/<session_id>` - Retrieve conversation history
- `GET /analytics` - Basic usage analytics

## 🎨 Frontend Features

- **Glassmorphism Design**: Modern, professional appearance
- **Real-time Stats**: Message counts, response times, session duration
- **Mobile Responsive**: Works perfectly on phones and tablets
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Error Handling**: User-friendly error messages and retry mechanisms
- **Quick Actions**: Mental health conversation starters
- **Crisis Resources**: Emergency contacts always visible

## 🔒 Security & Privacy

- Session-based conversation tracking
- No personal data stored beyond conversations
- Secure API key management via environment variables
- CORS configuration for web security

## 🚑 Crisis Support Integration

The interface includes prominent crisis resources:
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741
- Emergency Services: 911

## 📈 Analytics & Monitoring

- Real-time response time tracking
- Message frequency analysis
- Session duration monitoring
- Error rate tracking
- User engagement metrics

## 🤝 Support

This enhanced version maintains 100% compatibility with your original implementation while adding:
- Professional UI/UX design
- Data persistence and analytics
- Better error handling
- Mobile responsiveness
- Crisis resource integration

Your core AI pipeline using LangChain, Groq, and ChromaDB remains exactly as you designed it.
