# Quiz API

This is a simple Quiz API. It allows users to create quizzes, add questions to them, and take quizzes.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Installation

To install and run this API locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/KexySerJ90/Quiz_API.git
```

2. Install the dependencies:

```bash
cd Quiz_API
npm install
```

3. Create a `.env` file in the root directory and add the following environment variables:

```
MONGODB_URI=<your_mongodb_uri>
PORT=<port_number>
```

4. Start the server:

```bash
npm start
```

## Usage

Once the server is running, you can use tools like Postman or cURL to interact with the API endpoints. The API documentation is available at `/api-docs` endpoint.

## API Endpoints

The API provides the following endpoints:

- `GET /quizzes`: Get a list of all quizzes.
- `POST /quizzes`: Create a new quiz.
- `GET /quizzes/:id`: Get details of a specific quiz.
- `PUT /quizzes/:id`: Update a specific quiz.
- `DELETE /quizzes/:id`: Delete a specific quiz.
- `POST /quizzes/:id/questions`: Add a question to a specific quiz.
- `PUT /quizzes/:id/questions/:questionId`: Update a specific question in a specific quiz.
- `DELETE /quizzes/:id/questions/:questionId`: Delete a specific question from a specific quiz.
- `POST /quizzes/:id/take`: Take a specific quiz.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.
