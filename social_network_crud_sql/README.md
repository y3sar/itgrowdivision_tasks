# Simple Social Network CRUD App

This is a basic Python application that demonstrates CRUD operations (Create, Read, Update, Delete) for a simple social network using SQLite3 as the database.

## User Schema

The `users` table in the database has the following schema:

- **`id`**: INTEGER, PRIMARY KEY, AUTOINCREMENT. Unique identifier for each user.
- **`username`**: TEXT, NOT NULL. The username chosen by the user for identification.
- **`email`**: TEXT, NOT NULL. The email address of the user.
- **`bio`**: TEXT. An optional field for a brief user biography.

## User Schema Design

- **`id` (Primary Key)**: An auto-incremented integer is used as the primary key to ensure each user has a unique identifier. This is a common practice for user-related tables.

- **`username`**: A non-null text field is chosen for the username to ensure that each user has a username. Text is used as usernames can be alphanumeric and can include special characters.

- **`email`**: A non-null text field is chosen for the email address to ensure that each user has a unique email. Text is used as email addresses can contain alphanumeric characters and special characters.

- **`bio`**: A text field is used for the user's biography as it allows for a variable length description. This is optional to accommodate users who may not want to provide a bio.

## How to Use

1. **Setup Database**: Run the application to set up the SQLite database.

    ```bash
    python database.py
    ```

2. **Run test Script**: Execute the test script to see the CRUD operations in action.

    ```bash
    python test.py
    ```

## File Structure

- **`database.py`**: Initializes the database.
- **`user_crud.py`**: Defines CRUD functions.
- **`test.py`**: Example usage of CRUD functions.

## Notes

- This is a basic example and lacks advanced features, error handling, and security measures.
- Modify and extend the code based on the requirements of your application.

Feel free to explore, modify, and build upon this simple social network CRUD app!
