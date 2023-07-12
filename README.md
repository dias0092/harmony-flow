# Harmony Flow

Harmony Flow is a music streaming web application built using Django.

## Features

- User Registration and Login
- Browsing Artists, Albums, and Tracks
- Creation and Management of Playlists
- Follow/Unfollow functionality between users
- Song listening history
- User's song likes functionality
- Subscription plans and payments

## Setup and Installation

To get started, clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/harmony-flow.git
```

Navigate into the project directory:

    ```bash
    cd harmony-flow
    ```
    
Run the Django migrations to create your database schema:

    ```bash
    python manage.py migrate
    ```

Start the Django development server:

    ```bash
    python manage.py runserver
    ```

You should now be able to open your browser and navigate to `http://localhost:8000` to view the application.

## Running the Tests

To run the tests for this project, you can use the following command:

```bash
python manage.py test