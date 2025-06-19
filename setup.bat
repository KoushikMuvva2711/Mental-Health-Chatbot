@echo off
echo 🧠 Setting up Mental Health Chatbot Project...

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

REM Install dependencies
echo ⬇️ Installing dependencies...
pip install -r requirements.txt

REM Create templates directory
echo 📁 Creating templates directory...
if not exist templates mkdir templates

REM Move HTML file to templates
echo 📋 Moving frontend to templates...
move enhanced_index.html templates\

REM Create data directory if it doesn't exist
echo 📚 Creating data directory...
if not exist data mkdir data

REM Set up environment file
echo ⚙️ Setting up environment...
if not exist .env (
    copy .env.template .env
    echo ✅ Created .env file from template
    echo ⚠️ Please update your paths in .env file
) else (
    echo ℹ️ .env file already exists
)

echo.
echo 🎉 Setup complete!
echo.
echo 📋 Next steps:
echo 1. Update the DOCS_DIRECTORY path in .env file
echo 2. Add your PDF documents to the data directory
echo 3. Update GROQ_API_KEY if needed
echo 4. Run: python enhanced_app.py
echo.
echo 🌐 The application will be available at: http://localhost:5000
pause
