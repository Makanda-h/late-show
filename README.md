# Late Show Project

# Introduction
Building a Flask API to manage episodes, guests, and their appearances on particular episodes is the goal of this project. Managing data models and putting in place RESTful routes to enable communication with these models via HTTP requests are the main functionalities. An ER diagram, which determines the interactions between Episode, Guest, and Appearance items, serves as the foundation for the main relationships between models..

# Author 
Hope Makanda 

## Features

- Add new appearances
- View a list of all Guests and by id
- View a list of all episodes and 

## Installation

To install the Late Show Project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Makanda-h/late-show.git
    ```
2. Navigate to the project directory:
    ```bash
    cd late Show
    cd server
    ```
3. Install the dependencies:
    ```bash
    npm install
    ```
4. Navigate into the virtual environment
   ```bash
   pipenv install
   pipenv shell
   ```

## Usage

To start the application, run:
```bash
flask run 
```

Open your browser and navigate to `http://localhost:5000` to start using the LateShow API.

# Testing
You can test progress using Thunder client to make requests to the Flask API.

## License

This project is licensed under the MIT License. 