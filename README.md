# Harmony Flow

Harmony Flow is a music streaming web application built using Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11
- Django 4.2

## Features

- User Registration and Login
- Browsing Artists, Albums, and Tracks
- Creation and Management of Playlists
- Follow/Unfollow functionality between users
- Song listening history
- User's song likes functionality
- Subscription plans and payments


## Setup and Installation

1. To get started, clone this repository to your local machine.

    ```bash
    git clone https://github.com/dias0092/harmony-flow.git
    ```

2. Navigate into the project directory:

    ```bash
    cd harmony-flow
    ```

3. Install the dependencies using Pipenv:

    ```bash
    pipenv install
    ```
    

4. Activate the Pipenv shell:

    ```bash
    pipenv shell
    ```
    
    
5. Run the Django migrations to create your database schema:

    ```bash
    python manage.py migrate
    ```

6. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

You should now be able to open your browser and navigate to `http://localhost:8000` to view the application.

## Running the Tests

To run the tests for this project, you can use the following command:

```bash
python manage.py test
