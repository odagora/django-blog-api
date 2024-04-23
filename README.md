# README

This project is a Django CRUD API for a blog. It includes models for Authors, Categories, Posts, and Comments. The project settings are configured for development with debug mode enabled. The API uses Django Rest Framework and includes CORS headers for cross-origin requests.

## Setup
1. Clone the repository.
2. Install virtual environment with `python3 -m venv venv`.
3. Activate the virtual environment with `source venv/bin/activate`.
4. Install dependencies using `pip install -r requirements.txt`.
5. Apply migrations with `python manage.py migrate blog`.
6. Create a new super user with `python manage.py createsuperuser`

## Running the Server
Run the development server with `python manage.py runserver`.

## Endpoints
- `/admin`: Django admin panel (login with your super user credentials).
- `/blog`: Main blog app page.
- `blog/docs`: API documentation page.
- `blog/api/v1/posts/`: Endpoint for managing blog posts.
- `blog/api/v1/authors/`: Endpoint for managing authors.
- `blog/api/v1/categories/`: Endpoint for managing categories.
- `blog/api/v1/comments/`: Endpoint for managing comments.

## Testing
Basic test setup is available in `blog/tests.py`. Run tests with `python manage.py test`.

## Additional Notes
- Ensure to set a secure `SECRET_KEY` in production settings.
- Update `ALLOWED_HOSTS` for production deployment.
- Customize settings for internationalization, time zone, and static files as needed.
- Configure CORS origins in `CORS_ALLOWED_ORIGINS` (see the example for `localhost`):
  ```python
    CORS_ALLOWED_ORIGINS = [
      'http://localhost:8000'
    ]
  ```