# Test with BFF OptiPrice v1 - Django Backend for Frontend

A comprehensive Django-based Backend for Frontend (BFF) application specifically designed for the OptiPrice system. Built with enterprise-grade patterns for scalability and maintainability.

## 🏗️ Architecture

- **Django 5.2.8** with **Django REST Framework 3.16.1** - Modern API framework
- **JSON:API compliant** REST API with camelCase serialization
- **PostgreSQL 15** with **PGBouncer** connection pooling - High-performance database layer
- **Redis 5.0.1** with **django-cachalot** - Advanced ORM query caching and session storage
- **RabbitMQ** with **Celery 5.5.3** - Distributed task processing and message queuing
- **SAML2 SSO** via **djangosaml2** with **Keycloak** IdP - Enterprise authentication
- **OpenAPI/Swagger** documentation via **drf-spectacular** - Auto-generated API docs
- **Docker** multi-service containerization - Production-ready deployment

## 🚀 Quick Start

### Automated SSO Setup (Recommended)

Get everything running with complete SAML2 SSO in one command:

```bash
# Complete automated setup
pip install locally and run the server

```

```bash
# Complete automated setup
make setup-sso

# Test SSO functionality
make sso-test
```

This automatically:
- ✅ Builds containers with SSL certificates
- ✅ Starts all services (PostgreSQL, Redis, RabbitMQ, Django, Keycloak)
- ✅ Configures Keycloak realm and SAML client
- ✅ Creates test users with OptiPrice groups (admin.user/admin123, test.user/test123, emea.user/emea123)
- ✅ Sets up complete SAML2 SSO flow

### Manual Docker Setup

```bash
# Start all services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f
```

### Prerequisites

- Docker and Docker Compose
- Python 3.12+ (for local development)
- Make (optional, for convenience commands)

### Local Development Setup

```bash
# Install dependencies
make install-dev

# Set up pre-commit hooks
make setup-pre-commit

# Run migrations
make django-migrate

# Create superuser
make django-createsuperuser
```

## 📋 Available Services

| Service | Port | URL | Description |
|---------|------|-----|-------------|
| Django API | 8000 | http://localhost:8000 | Main application |
| **SSO Login** | 8000 | http://localhost:8000/api/v1/user/sso/login/ | **SAML SSO Login** |
| **Keycloak IdP** | 8080 | http://localhost:8080 | **Identity Provider** |
| PostgreSQL | 5432 | - | Database |
| PgBouncer | 6432 | - | Connection pooler |
| Redis | 6379 | - | Cache & message backend |
| RabbitMQ | 5672 | - | Message broker |
| RabbitMQ Management | 15672 | http://localhost:15672 | RabbitMQ admin |
| Flower | 5555 | http://localhost:5555 | Celery monitoring |

### 🔐 SSO Test Credentials

- **Admin User**: `admin.user` / `admin123` (all OptiPrice groups - full access)
- **Test User**: `test.user` / `test123` (NAMR region, Vans brand, web/full-price channels)
- **EMEA User**: `emea.user` / `emea123` (EMEA region, Timberland/North Face brands, outlet/full-price channels)
- **Keycloak Admin**: `admin` / `admin`

**OptiPrice Groups**: NAMR/EMEA/APAC regions, TB/VN/NF brands, FULL_PRICE/OUTLET/WEB channels, ADMIN/STORE/VIEWER roles

## 🛠️ Development Tools

This project uses comprehensive code quality tools:

### Pre-commit Hooks

- **black** - Code formatting
- **isort** - Import sorting
- **flake8** - Linting
- **pylint** - Advanced linting
- **tartufo** - Secret scanning
- **bandit** - Security analysis
- **mypy** - Type checking

### Usage Commands

```bash
# Format code
make format

# Run linting
make lint

# Run security checks
make security

# Run all pre-commit hooks
make pre-commit

# Run tests with coverage
make coverage

# SSO commands
make setup-sso          # Complete automated SSO setup
make sso-health         # Check SSO health
make sso-test          # Test SSO flow
make sso-logs          # View SSO logs
make setup-sso-manual  # Manual Keycloak config
```

## 📁 Project Structure

```
bff-optiprice-v2/
├── src/
│   ├── apps/
│   │   ├── ap_cluster/      # Automated Pricing: Cluster management
│   │   ├── ap_core/         # Automated Pricing: Core functionality & configs
│   │   ├── ap_dc/           # Automated Pricing: Data collection
│   │   ├── ap_plan/         # Automated Pricing: Planning and strategy
│   │   ├── ap_product/      # Automated Pricing: Product management
│   │   ├── ap_rank/         # Automated Pricing: Ranking algorithms
│   │   ├── ap_taxonomy/     # Automated Pricing: Product taxonomy
│   │   ├── catalog/         # Product catalog management
│   │   ├── context/         # Context data (brands, regions, countries, currencies)
│   │   ├── core/            # Core utilities and shared components
│   │   ├── governance/      # Business governance and rules
│   │   ├── integration/     # External system integrations
│   │   ├── ir_opportunity/  # Inventory reconciliation opportunities
│   │   ├── markdown/        # Markdown processing
│   │   ├── op_catalog/      # OptiPrice catalog features
│   │   ├── op_governance/   # OptiPrice governance
│   │   ├── op_integration/  # OptiPrice integrations
│   │   ├── op_markdown/     # OptiPrice markdown
│   │   ├── op_overview/     # OptiPrice overview dashboards
│   │   ├── overview/        # General overview features
│   │   └── user/            # User management and authentication
│   ├── bff_ibp_console/
│   │   ├── settings/        # Modular Django settings
│   │   │   ├── base.py      # Base configuration
│   │   │   ├── development.py # Development settings
│   │   │   ├── production.py  # Production settings
│   │   │   ├── saml2.py     # SAML2 SSO configuration
│   │   │   └── drf.py       # Django REST Framework settings
│   │   ├── asgi.py          # ASGI configuration
│   │   ├── celery.py        # Celery configuration
│   │   ├── urls.py          # Main URL routing
│   │   └── wsgi.py          # WSGI configuration
│   ├── docker-compose.yml   # Multi-service Docker orchestration
│   ├── requirements.txt     # Production dependencies
│   ├── requirements-dev.txt # Development dependencies
│   └── manage.py           # Django management script
├── certs/                  # SSL certificates for SAML
├── keycloak/              # Keycloak configuration and realm
├── scripts/               # Deployment and utility scripts
├── ci-cd/                 # CI/CD pipeline configuration
├── charts/                # Kubernetes Helm charts
├── Dockerfile             # Django application container
├── Makefile              # Development automation commands
├── CLAUDE.md             # Project configuration guide
└── README.md             # Project documentation
```

## 🔧 Configuration Files

### Code Quality
- `.pre-commit-config.yaml` - Pre-commit configuration
- `.pylintrc` - Pylint settings
- `.flake8` - Flake8 settings
- `pyproject.toml` - Black, isort, and other tool configs
- `.tartufo.toml` - Secret scanning config

### Docker
- `docker-compose.yml` - Service definitions
- `Dockerfile` - Django app container
- `init-db.sql` - Database initialization

## 🌍 Environment Variables

Copy `.env.example` to `.env` and configure:

## 🧪 Testing

```bash
# Run tests
make test

# Run with coverage
make coverage

# Run specific test
docker-compose exec web python manage.py test apps.api.tests.test_views
```

## 📊 API Endpoints

### Authentication & SSO
- `GET /api/v1/user/sso/login/` - Initiate SAML SSO login
- `POST /api/v1/user/sso/callback/` - SAML assertion callback (ACS)
- `GET /api/v1/user/sso/logout/` - SSO logout
- `GET /api/v1/user/sso/health/` - SSO health check
- `GET /api/v1/user/sso/metadata/` - SAML metadata

### Automated Pricing (AP) APIs
- **Core**: `/api/v1/ap/core/` - General configuration and settings
- **Cluster**: `/api/v1/ap/cluster/` - Product cluster management
- **Data Collection**: `/api/v1/ap/dc/` - Data collection processes
- **Planning**: `/api/v1/ap/plan/` - Pricing strategy and planning
- **Product**: `/api/v1/ap/product/` - Product management
- **Ranking**: `/api/v1/ap/rank/` - Product ranking algorithms
- **Taxonomy**: `/api/v1/ap/taxonomy/` - Product classification

### OptiPrice Platform APIs
- **Catalog**: `/api/v1/op/catalog/` - Product catalog features
- **Governance**: `/api/v1/op/governance/` - Business rules and governance
- **Integration**: `/api/v1/op/integration/` - External system integrations
- **Markdown**: `/api/v1/op/markdown/` - Price markdown processing
- **Overview**: `/api/v1/op/overview/` - Dashboard and overview data

### Business Intelligence
- **IR Opportunities**: `/api/v1/ir/opportunity/` - Inventory reconciliation opportunities
- **Context Data**: `/api/v1/context/` - Brands, regions, countries, currencies

### System APIs
- **Health Check**: `/api/v1/core/health/` - System health monitoring
- **Task Management**: `/api/v1/core/tasks/` - Background task management

### Documentation
- **API Schema**: `/api/schema/` - OpenAPI 3.0 specification
- **Swagger UI**: `/api/schema/swagger-ui/` - Interactive API documentation
- **ReDoc**: `/api/schema/redoc/` - Alternative API documentation

## 🔄 Celery Tasks & Background Processing

The project includes comprehensive background task processing with Celery:

### Task Queues
- **High Priority Queue**: Critical pricing calculations and real-time updates
- **Default Queue**: Standard data processing and API operations
- **Low Priority Queue**: Bulk data imports, reports, and maintenance tasks

### Key Background Tasks
- **Data Synchronization**: Regular sync with external pricing systems
- **Pricing Calculations**: Complex algorithmic pricing computations
- **Report Generation**: Automated report creation and distribution
- **Data Validation**: Quality checks and data integrity processes
- **Cache Management**: Intelligent cache warming and invalidation

### Monitoring & Management
- **Flower Dashboard**: Real-time task monitoring at http://localhost:5555
- **Task Scheduling**: Periodic tasks via django-celery-beat
- **Error Handling**: Comprehensive retry logic and failure notifications

### Usage Examples
```python
# Trigger pricing calculation
from apps.ap_core.tasks import calculate_pricing_strategy
result = calculate_pricing_strategy.delay(product_ids, strategy_params)

# Schedule data sync
from apps.integration.tasks import sync_external_data
sync_external_data.apply_async(countdown=60)  # Execute after 1 minute
```

## 📝 Development Workflow

1. **Clone and Setup**: `git clone <repo> && cd bff-optiprice-v2 && make setup-sso`
2. **Feature Development**: Create feature branch and implement changes
3. **Code Quality**: Pre-commit hooks automatically run (black, isort, flake8, pylint, security checks)
4. **Testing**: Run comprehensive test suite with `make test-coverage`
5. **Documentation**: Update API docs if endpoints change
6. **Integration**: Verify SSO and all services work with `make sso-test && make health-check`

```bash
# Complete development cycle
make format && make lint && make test-coverage && make sso-test
```

### Data Management
```bash
# Create synthetic test data for all AP modules
make create-all-syntetic-data

# Dry run to see what data would be created
make create-ap-synthetic-data-dry-run
```

## 🚨 Troubleshooting

### Common Issues

**Docker services not starting:**
```bash
docker-compose down
docker-compose up --build
```

**Database connection errors:**
```bash
docker-compose logs postgres
docker-compose exec web python manage.py migrate
```

**Pre-commit issues:**
```bash
pre-commit clean
pre-commit install
```

**SSO/Keycloak issues:**
```bash
# Check SSO health and configuration
make sso-health

# View SSO-related logs
make sso-logs

# Reset SSO setup if needed
make setup-sso-manual
```

**Permission errors:**
```bash
sudo chown -R $USER:$USER .
```

**Service health checks:**
```bash
# Verify all services are running correctly
make health-check

# Check individual service logs
docker-compose logs postgres
docker-compose logs redis
docker-compose logs rabbitmq
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/VFAP-12345-description`
3. **Set up development environment**: `make setup-sso`
4. **Make your changes** following the project patterns
5. **Run quality checks**: `make format && make lint && make security`
6. **Test thoroughly**: `make test-coverage`
7. **Verify integration**: `make sso-test && make health-check`
8. **Commit changes** (pre-commit hooks will run automatically)
9. **Push to your branch** and create a Pull Request

### Code Standards
- Follow existing Django app patterns and naming conventions
- Write comprehensive tests for new functionality
- Ensure all linting and security checks pass
- Document new API endpoints in docstrings
- Update CLAUDE.md if adding new features or configuration

## 📚 Additional Resources

- **CLAUDE.md**: Comprehensive project configuration guide
- **API Documentation**: http://localhost:8000/api/schema/swagger-ui/
- **Keycloak Documentation**: https://www.keycloak.org/documentation
- **Django REST Framework**: https://www.django-rest-framework.org/
- **Celery Documentation**: https://docs.celeryproject.org/

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
