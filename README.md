# Database CRUD Operations Console



## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Examples](#Examples)
  - [Example 1: Database Migrations with Alembic](#Example-1-database-migrations-with-alembic)
  - [Example 2: CRUD Operations](#Example-2-crud-operations)
  - [Example 3: Seeding Sample Data](#Example-3-seeding-sample-data)
  - [Example 4: CLI for Database Operations](#Example-4-cli-for-database-operations)
  - [Example 5: Advanced Database Queries](#Example-5-advanced-database-queries)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Examples and code examples, follow these steps:

1. Clone the repository:
git clone <repository-url>


2. Install Poetry:
curl -sSL https://install.python-poetry.org | python3 -



3. Install the project dependencies:
poetry install


4. Set up the database configuration:
- Modify the `config.ini` file with your database credentials.
- Ensure that the required database is set up and accessible.

5. Run the code examples and Examples using Poetry:
poetry run python script_name.py



## Example 

### Example 1: Database Migrations with Alembic

Learn how to manage database migrations using Alembic, a powerful database migration tool for SQLAlchemy. Understand the process of synchronizing the database schema with your application code as it evolves over time.

Example Highlights:
- Setting up Alembic configuration
- Creating and running migrations
- Handling offline and online migrations

### Example 2: CRUD Operations

Master the basic CRUD operations (Create, Read, Update, Delete) in SQLAlchemy. Explore different techniques for creating, reading, updating, and deleting records from a database using SQLAlchemy's powerful ORM capabilities.

Example Highlights:
- Creating records
- Retrieving records
- Updating records
- Deleting records

### Example 3: Seeding Sample Data

Learn how to seed your database with sample data using Faker, a Python library for generating fake data. Discover techniques for populating your database with realistic test data to facilitate development and testing.

Example Highlights:
- Generating fake data with Faker
- Seeding records for teachers, students, subjects, grades, and groups

### Example 4: CLI for Database Operations

Build a command-line interface (CLI) tool to perform database operations. Create a user-friendly interface that allows users to execute CRUD operations on the database using command-line arguments.

Example Highlights:
- Parsing command-line arguments with argparse
- Implementing create, read, update, and delete functionality
- Handling exceptions and error messages

### Example 5: Advanced Database Queries

Explore advanced database query techniques using SQLAlchemy. Learn how to perform complex queries to retrieve specific information from the database, such as aggregations, filtering, sorting, and joining multiple tables.

Example Highlights:
- Aggregating data and calculating averages
- Filtering and sorting results
- Joining tables and retrieving related data
- Executing complex queries

## Contributing

Contributions to this repository are welcome! If you have any improvements, bug fixes, or additional Examples/code examples to share, feel free to submit a pull request or open an issue. Let's learn and grow together!

## License

This project is licensed under the [MIT License](LICENSE).
