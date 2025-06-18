#!/bin/bash

# SmartDocs Development Startup Script
echo "🚀 Starting SmartDocs Development Environment..."

# Navigate to backend directory
cd backend

# Check if virtual environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Virtual environment not detected. Please activate it first:"
    echo "   python -m venv venv"
    echo "   source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
    echo "   pip install -r requirements-basic.txt"
    echo ""
fi

# Install basic dependencies if needed
echo "📦 Installing dependencies..."
pip install -r requirements-basic.txt

# Run migrations
echo "🔄 Running migrations..."
python manage.py migrate --settings=config.settings_local

# Create superuser if it doesn't exist
echo "👤 Creating superuser (if needed)..."
python manage.py shell --settings=config.settings_local -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@smartdocs.com', 'admin123')
    print('✅ Superuser created: admin/admin123')
else:
    print('✅ Superuser already exists: admin/admin123')
"

# Start development server
echo "🌐 Starting development server..."
echo "📍 Server will be available at: http://127.0.0.1:8000"
echo "📍 API Documentation: http://127.0.0.1:8000/api/docs/"
echo "📍 Admin Panel: http://127.0.0.1:8000/admin/"
echo ""
echo "🔑 Admin credentials: admin/admin123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver --settings=config.settings_local 127.0.0.1:8000 