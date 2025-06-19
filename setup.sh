#!/bin/bash
# Mental Health Chatbot Setup Script

echo "🧠 Setting up Mental Health Chatbot Project..."

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate || venv\Scripts\activate

# Install dependencies
echo "⬇️ Installing dependencies..."
pip install -r requirements.txt

# Create templates directory
echo "📁 Creating templates directory..."
mkdir -p templates

# Move HTML file to templates
echo "📋 Moving frontend to templates..."
mv enhanced_index.html templates/

# Create data directory if it doesn't exist
echo "📚 Creating data directory..."
mkdir -p data

# Set up environment file
echo "⚙️ Setting up environment..."
if [ ! -f .env ]; then
    cp .env.template .env
    echo "✅ Created .env file from template"
    echo "⚠️ Please update your paths in .env file"
else
    echo "ℹ️ .env file already exists"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Update the DOCS_DIRECTORY path in .env file"
echo "2. Add your PDF documents to the data directory"
echo "3. Update GROQ_API_KEY if needed"
echo "4. Run: python enhanced_app.py"
echo ""
echo "🌐 The application will be available at: http://localhost:5000"
