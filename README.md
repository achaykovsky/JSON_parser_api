# Flask Application - JSON Data Management and Validation

## Overview

This Flask application provides a simple API for managing and validating JSON data. It allows users to retrieve, update, and delete key-value pairs, validate JSON objects based on a specified maximum depth, and handle errors gracefully. The application is designed to be flexible and easily extendable, making it a useful tool for managing JSON data in a web environment.

## Features

- **Index Route**: Displays a welcome message to indicate that the server is running.
- **Validate JSON**: Validates a JSON object based on a specified maximum depth.
- **Data Management**: Allows retrieval, update, and deletion of key-value pairs in a global `data_content` dictionary.
- **Error Handling**: Provides custom error handling for 404 errors (Page Not Found).

## Endpoints

### `GET /`

- **Description**: Returns a welcome message.
- **Response**: 
  ```json
  {
    "message": "Welcome to the templates app server!"
  }
  ```

### `POST /validate_json`

- **Description**: Validates a JSON object based on a specified maximum depth.
- **Request Parameters**:
  - `max_depth` (optional, default: 2): The maximum allowed depth of the JSON object.
- **Request Body**:
  - A JSON object to be validated.
- **Response**:
  - If the JSON is valid:
    ```json
    {
      "valid": true
    }
    ```
  - If the JSON is invalid:
    ```json
    {
      "valid": false,
      "error": "Provided data is not a valid JSON object"
    }
    ```

### `GET /data`

- **Description**: Returns the entire `data_content` dictionary.
- **Response**:
  ```json
  {
    "key_1": "value_1",
    "key_2": "value_2"
  }
  ```

### `GET /data/<key>`

- **Description**: Retrieves the value associated with a specified key in `data_content`.
- **Request Parameters**:
  - `key`: The key for which the value should be retrieved.
- **Response**:
  - If the key is found:
    ```json
    {
      "key": "value"
    }
    ```
  - If the key is not found:
    ```json
    {
      "message": "The requested parameter <key> was not found"
    }
    ```

### `DELETE /data/delete/<key>`

- **Description**: Deletes a key-value pair from `data_content`.
- **Request Parameters**:
  - `key`: The key to be deleted.
- **Response**:
  - If the key is found and deleted:
    ```json
    {
      "message": "Parameter <key> and its content was deleted successfully"
    }
    ```
  - If the key is not found:
    ```json
    {
      "message": "The parameter <key> was not found"
    }
    ```

### `PUT /update-data`

- **Description**: Updates the `data_content` dictionary with new key-value pairs.
- **Request Body**:
  - A JSON object containing key-value pairs to be added or updated in `data_content`.
- **Response**:
  ```json
  {
    "data_content": {
      "key_1": "value_1",
      "key_2": "value_2",
      ...
    }
  }
  ```

### `GET /<error_route>`

- **Description**: Handles non-existent routes and returns a 404 error message.
- **Response**:
  ```json
  {
    "error": "404 Not Found: The requested URL was not found on the server."
  }
  ```

## Running the Application

To run the application, execute the following command in your terminal:

```bash
python app.py
```

The server will start on `http://0.0.0.0:5000/` and can be accessed via a web browser or a tool like `curl` or Postman.

## Dependencies

- **Flask**: A lightweight WSGI web application framework for Python.
- **validate_json**: A custom module to validate the structure of JSON objects.

To install the dependencies, run:

```bash
pip install Flask
```

## Customization

- Modify the `data_content` dictionary to suit your data management needs.
- Customize the JSON validation logic in `validate_json` to meet specific requirements.
- Extend the error handling to cover additional cases as needed.

## License

This project is open-source and available under the MIT License.
