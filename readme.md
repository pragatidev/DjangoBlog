# Django Blog Web App

This is a simple Django web application that allows users to write and publish blog posts. Users can create accounts, log in, and create, edit, and delete their own posts. The application also allows users to comment on posts.

## Installation

1. Clone the repository: `git clone https://github.com/pragatidev/BlogWebApp.git`
2. Navigate into the project directory: `cd BlogWebApp`
3. Create and activate a virtual environment:
   - On Windows: `python -m venv venv` followed by `venv\Scripts\activate`
   - On macOS/Linux: `python3 -m venv venv` followed by `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Copy the .env.example file to .env and replace the `your_secret_key_here` value with a new secret key of your choice.
   - On Windows: `copy .env.example .env`
   - On macOS/Linux: `cp .env.example .env`
6. Migrate the database: `python manage.py migrate`

## Usage

1. Run the development server: `python manage.py runserver`
2. Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Deployment

The application can be deployed to a production server using any hosting provider that supports Django web applications. Some popular options include:

- [Heroku](https://www.heroku.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
- [DigitalOcean](https://www.digitalocean.com/)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

## Features

- User authentication and authorization
- Create, edit, and delete blog posts
- Publish and unpublish blog posts
- Comment on blog posts
- Pagination of blog posts

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Loading the Secret Key from .env

In order to load the SECRET_KEY variable from the .env file, add the following lines to the settings.py file:

```python
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
