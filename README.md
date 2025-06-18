# 🎯 SmartDocs - AI-Powered Document Analysis SaaS

A comprehensive SaaS platform for intelligent document analysis using AI, OCR, and machine learning technologies.

## 🛠️ Technology Stack

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Primary database
- **Redis** - Caching and message broker
- **Celery** - Asynchronous task processing
- **Docker** - Containerization

### AI/ML & OCR
- **PyTesseract** - OCR text extraction
- **EasyOCR** - Advanced OCR capabilities  
- **spaCy** - Natural language processing
- **transformers** - Hugging Face transformers

### Frontend
- **React** - UI library
- **Vite** - Build tool
- **TailwindCSS** - Styling framework

### DevOps
- **Docker Compose** - Multi-container orchestration
- **GitHub Actions** - CI/CD pipeline
- **Railway/Render/Vercel** - Deployment platforms

## 🏗️ Project Structure

```
saas/
├── backend/
│   ├── config/                 # Django project configuration
│   │   ├── __init__.py
│   │   ├── settings.py         # Django settings
│   │   ├── urls.py            # Main URL configuration
│   │   ├── wsgi.py            # WSGI configuration
│   │   └── celery.py          # Celery configuration
│   ├── apps/                  # Django applications
│   │   ├── __init__.py
│   │   ├── core/              # Core functionality
│   │   ├── users/             # User management & auth
│   │   └── documents/         # Document management
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile            # Backend Docker configuration
│   ├── .dockerignore         # Docker ignore file
│   └── env.example           # Environment variables template
├── frontend/
│   └── Dockerfile            # Frontend Docker configuration
├── docker-compose.yml        # Multi-service Docker setup
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ (3.11 recommended)
- Node.js 18+
- Git

### 🎯 **FASTEST WAY TO START** (Recommended)

1. **Clone and enter the project**
   ```bash
   git clone <repository-url>
   cd saas
   ```

2. **Run the development script**
   ```bash
   ./start_dev.sh
   ```

That's it! The script will:
- ✅ Install all dependencies
- ✅ Set up SQLite database 
- ✅ Run migrations
- ✅ Create admin user (admin/admin123)
- ✅ Start the development server

**🌐 Access your services:**
- **Backend API**: http://127.0.0.1:8000
- **API Documentation**: http://127.0.0.1:8000/api/docs/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Health Check**: http://127.0.0.1:8000/api/v1/core/health/

### 🔧 Manual Setup (Alternative)

1. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-basic.txt
   python manage.py migrate --settings=config.settings_local
   python manage.py createsuperuser --settings=config.settings_local
   python manage.py runserver --settings=config.settings_local
   ```

### 🐳 Docker Setup (Production-like)

1. **Environment Setup**
   ```bash
   cp backend/env.example backend/.env
   # Edit backend/.env with your configuration
   ```

2. **Start with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Services will be available at:**
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/api/docs/
   - Frontend: http://localhost:3000
   - PostgreSQL: localhost:5432
   - Redis: localhost:6379

## 📚 API Documentation

Once the backend is running, you can access:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/

## 🔑 Available Endpoints

### Authentication
- `POST /api/v1/auth/register/` - User registration
- `POST /api/v1/auth/login/` - User login
- `GET /api/v1/auth/profile/` - User profile

### Core
- `GET /api/v1/core/health/` - Health check

### Documents (Coming Soon)
- `GET /api/v1/documents/` - List documents
- `POST /api/v1/documents/upload/` - Upload document
- `GET /api/v1/documents/{id}/` - Document details
- `POST /api/v1/documents/{id}/analyze/` - Analyze document

## 🔧 Environment Variables

Copy `backend/env.example` to `backend/.env` and configure:

### Django Settings
- `DEBUG` - Debug mode (True/False)
- `SECRET_KEY` - Django secret key
- `ALLOWED_HOSTS` - Allowed hosts (comma-separated)

### Database
- `DATABASE_URL` - PostgreSQL connection URL
- `DB_NAME` - Database name
- `DB_USER` - Database user
- `DB_PASSWORD` - Database password
- `DB_HOST` - Database host
- `DB_PORT` - Database port

### Redis & Celery
- `REDIS_URL` - Redis connection URL
- `CELERY_BROKER_URL` - Celery broker URL
- `CELERY_RESULT_BACKEND` - Celery result backend URL

### OCR Settings
- `TESSERACT_CMD` - Tesseract command path
- `OCR_LANGUAGES` - OCR languages (comma-separated)

### Email Configuration
- `EMAIL_BACKEND` - Email backend
- `EMAIL_HOST` - SMTP host
- `EMAIL_PORT` - SMTP port
- `EMAIL_USE_TLS` - Use TLS (True/False)
- `EMAIL_HOST_USER` - SMTP username
- `EMAIL_HOST_PASSWORD` - SMTP password

## 🧪 Development Roadmap

### ✅ Week 1: Architecture + Basic Backend + API
- [x] Django project setup with Docker
- [x] PostgreSQL + Redis configuration
- [x] App structure (users, documents, core)
- [x] Basic API endpoints
- [x] JWT Authentication
- [x] API documentation with Swagger

### 📋 Week 2: Models + Database + Advanced Auth (Coming Next)
- [ ] User models and profiles
- [ ] Document models and relationships
- [ ] File upload handling
- [ ] Advanced authentication features
- [ ] Database migrations and seed data

### 📋 Week 3: OCR + AI Integration
- [ ] OCR text extraction
- [ ] Document preprocessing
- [ ] AI analysis pipeline
- [ ] Celery tasks for processing

### 📋 Week 4: Frontend Development
- [ ] React application setup
- [ ] Authentication UI
- [ ] Document upload interface
- [ ] Results dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions, please:

1. Check the [API documentation](http://localhost:8000/api/docs/)
2. Review the Docker logs: `docker-compose logs`
3. Create an issue in the repository

---

**Built with ❤️ for intelligent document processing** 