# REST Countries Django Application

A Django web application that fetches and displays country information from the REST Countries API. This application allows users to browse countries, view detailed information, and filter countries by region and other criteria.

## Features

- Country listing with search and filter capabilities
- Detailed country information pages
- Region-based filtering
- User authentication and registration
- Responsive design using Bootstrap

## Tech Stack

- Python 3.10+
- Django 5.2
- Django REST Framework
- PostgreSQL
- Bootstrap 5
- Docker & Docker Compose

## Prerequisites

- Docker and Docker Compose
- Git

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/kaziiriad/rest_countries.git
cd rest-countries
```

### Environment Setup

Create a `.env` file in the project root with the following variables:

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://postgres:postgres@db:5432/rest_countries
```

### Running with Docker

1. Build and start the containers:

```bash
docker-compose up -d
```

2. The application should now be running at http://localhost:8000

### Initial Data Setup

The application comes with a management command to fetch country data from the REST Countries API:

```bash
docker-compose exec app python manage.py fetch_countries
```

This command will populate your database with country information.

## Project Structure

```
rest_countries/
├── core/                  # Main application
│   ├── management/        # Custom management commands
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   └── ...
├── rest_countries/        # Project settings
├── docker-compose.yml     # Docker configuration
├── Dockerfile             # Docker build instructions
└── pyproject.toml         # Python dependencies
```

## Usage

### User Registration and Login

- Navigate to `/accounts/register/` to create a new account
- Login at `/accounts/login/`
<!-- - After logging in, you can access country list and details -->

### Browsing Countries
- Country list is available at `/countries/`
- Country details are available at `/countries/<country_id>/`
- Filter countries by region and language
- Use the search box to find countries by name

### API Endpoints
- `/api/countries/` - List all countries
- `/api/countries/<country_id>/` - Get details of a specific country
- `/api/countries/?region=<region>/` - Filter countries by region
- `/api/countries/?lang=<language>/` - Filter countries by language
- `/api/countries/?search=<query>/` - Search countries by name

### Country Details

Click on any country to view detailed information including:
- Flag
- Capital
- Population
- Region
- Languages
- Timezones

## Development

### Making Migrations

```bash
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
```

## Deployment

For production deployment:

1. Set `DEBUG=False` in your `.env` file
2. Generate a new secure `SECRET_KEY`
3. Configure a proper database connection
4. Set up a reverse proxy (Nginx, etc.)
5. Configure static file serving

## License

[MIT License](LICENSE)

## Acknowledgements

- [REST Countries API](https://restcountries.com/) for providing the country data
- [Django](https://www.djangoproject.com/) web framework
- [Bootstrap](https://getbootstrap.com/) for the UI components
