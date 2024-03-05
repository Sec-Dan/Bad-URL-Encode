# Bad URL Encoder/Decoder

This Flask application provides a simple interface for encoding and decoding URLs. It replaces periods (`.`) in URLs with `[.]` during encoding and reverses the process during decoding.

## Features

- Encode URLs by replacing periods with `[.]`.
- Decode URLs by converting `[.]` back to periods.
- User-friendly web interface with a cool background.
- Copy encoded or decoded URL to clipboard functionality.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need to have Python installed on your machine. The application was developed with Python 3.9, but it should work with newer versions as well.

### Installing

First, clone the repository to your local machine:

> ```bash
> git clone https://github.com/yourusername/yourrepositoryname.git
> ```

Navigate to the project directory:

> ```bash
> cd yourrepositoryname
> ```

Install the required packages:

> ```bash
> pip install -r requirements.txt
> ```

### Running the Application

To run the application locally, execute:

> ```bash
> python app.py
> ```

The application will be available at `http://127.0.0.1:5000/`.

## Deployment

This application is ready to be deployed on Heroku with the provided `Procfile`. For detailed instructions on deploying to Heroku, please see the [Heroku official documentation](https://devcenter.heroku.com/articles/getting-started-with-python).

## Built With

- [Flask](https://palletsprojects.com/p/flask/) - The web framework used.
- [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server for UNIX, used for deploying the application on Heroku.
