# 1. Testing the Inventory of Devices Web API

## Objective

- Familiarize yourself with a Flask-based web API project.
- Understand the Docker and Docker Compose configuration used in the project.
- Interact with the Inventory of Devices API to understand its functionality.
- Develop test cases for this API (manual testing, no automation required yet).

## Tasks

### Clone the project repository

URL [https://github.com/waad19/mock-api-server](https://github.com/waad19/mock-api-server)

### Understand Docker and Docker Compose configuration
- Understand the services defined in `docker-compose.yml`.
- Note how the web server is containerized and how it interacts with other services.
- Identify the exposed ports and environment variables.

### Set up and run the application
- Install Docker and Docker Compose if not already installed.
- Verify the application is running:
    - Use a tool like `curl` or Postman.

### Interact with the Inventory of Devices API
- Use Postman, cURL, or any REST client of your choice.
    - Identify the available API endpoints related to the inventory of devices.
    - Analyze the request and response formats.

### Develop test cases for the Inventory of Devices API

- Write at least `5` test cases.
- Focus on both positive and negative scenarios.
- Consider edge cases and input validation, if applicable.
- Test case format:
    - `Test Case ID`: Unique identifier (e.g., TC_INV_001).
    - `Title/Description`: Brief description of what the test case validates.
    - `Pre-conditions`: Any setup required before executing the test.
    - `Test Steps`: Step-by-step instructions to perform the test.
    - `Expected Result`: The expected outcome after performing the test steps.
    - `Actual Result`: Leave blank for now; this will be filled during execution.
    - `Status`: Pass/Fail (leave as 'Not Executed' for now).
    - `Notes`: Any additional information or observations.

- Example test case

     ```
     Test Case ID: TC_INV_001
     Title: Verify adding a new device to the inventory
     Pre-conditions: API server is running; no device exists with ID '12345'
     Test Steps:
       1. Send a POST request to `/api/devices` with device data:
          {
            "id": "12345",
            "name": "Device A",
            "type": "Sensor",
            "status": "Active"
          }
     Expected Result:
       - The API returns a 201 Created status.
       - The response body contains the device data with a confirmation message.
     ```

### Implement test cases for the Inventory of Devices API

> [!NOTE]  
> Updated task section

- Automate your test cases using Python.
    - Use `pytest` and `requests` libraries.
    - Can be a simple single module with test functions.

### Add HTTPS configuration to Python tests

> [!NOTE]  
> Updated task section

- Investigate [inventory_files.py](app/routes/inventory_files.py) endpoints that return HTTPS encryption certificates.
- Investiagte how `requests` library can be configured to trust self-signed HTTPS certificates.
- Modify your Python tests to use either HTTP or HTTPS backend with appropriate configuration.
    - You can use JSON configuration file a boolean value to either enable or disable HTTPS and its configuration.

> [!IMPORTANT]  
> Create a fork of this repository and provide a link to it when you are ready to deliver. If you already have a fork - use it to complete all tasks.

# 2. Database Exploration and Testing

## Objective

- Connect to the database and run provided SQL queries, understanding their results.
- Write a simple Python test module that runs queries and checks the results.

## Tasks

### Investigate the database configuration

- Understand the `mock-database` service configuration defined in `docker-compose.yml`.
- Start the database service and connect to it using the credentials specified in configuration.
    - Use `psql`, pgAdmin, DBeaver, or any preferred PostgreSQL client.
- Execute the provided queries and note the output.
- Queries to execute:
    - **Retrieve top 10 most expensive products:**
       ```sql
       SELECT product_name, unit_price
       FROM products
       ORDER BY unit_price DESC
       LIMIT 10;
       ```
       - **`ORDER BY`**: Used to sort the result set in ascending or descending order.
       - **`DESC`**: Sorts the result in descending order.
       - **`LIMIT`**: Limits the number of rows returned.
       - Fetches `product_name` and `unit_price` of the top 10 most expensive products.
    - **Sum of freight charges by employee:**
       ```sql
       SELECT employee_id, SUM(freight)
       FROM orders
       GROUP BY employee_id;
       ```
       - **`SUM`**: An aggregate function that returns the sum of a numeric column.
       - Fetches `employee_id` and the sum of `freight` charges grouped by each employee.
    - **City-wise average, maximum, and minimum age of employees in London:**
       ```sql
       SELECT city,
         AVG(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))),
         MAX(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))),
         MIN(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date)))
       FROM employees
       WHERE city = 'London'
       GROUP BY city;
       ```
       - **`AVG`**, **`MAX`**, **`MIN`**: Aggregate functions to calculate average, maximum, and minimum values respectively.
       - **`CURRENT_TIMESTAMP`**: Returns the current date and time.
       - Fetches `city`, average age, maximum age, and minimum age of employees in London.
    - **City-wise average age of employees above 60:**
       ```sql
       SELECT city, AVG(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))) AS avg_age
       FROM employees
       GROUP BY city
       HAVING EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date)) > 60;
       ```
       - **`HAVING`**: Used to filter records that work on aggregated data.
       - Fetches `city` and average age of employees whose age is above 60, grouped by `city`.
    - **Retrieve top 3 oldest employees:**
       ```sql
       SELECT first_name, last_name, EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date)) AS age
       FROM employees
       ORDER BY age DESC
       LIMIT 3;
       ```
       - Fetches `first_name`, `last_name`, and age of the top 3 oldest employees.

### Write Python tests to verify database operation

- Install latest version of `psycopg2` to your virtual environment
- Write Python tests:
    - Verify that a connection to the database can be established.
    - Verify all the provided queries.
    - Use `pytest` fixtures for setting up and tearing down database connections.
- Avoid hardcoding sensitive information (e.g., username & password to the database) in your code.
  - Consider using environment variables or a configuration file (e.g., `.env` file with `python-dotenv`).

> [!IMPORTANT]  
> Create a fork of this repository and provide a link to it when you are ready to deliver. If you already have a fork - use it to complete all tasks.

# 3. Automate a Web UI Flow

## Objective
- Use Selenium to automate a simple website flow.

## Tasks

### The Web UI flow
- Website: [https://www.saucedemo.com/](https://www.saucedemo.com/)
- Credentials:
    - Username: `standard_user`
    - Password: `secret_sauce`
- Automation Steps:
    1. Login to the Website
        - Navigate to the Sauce Demo homepage.
        - Locate the username and password input fields and enter information.
        - Click the **Login** button.
    2. Add a product to the Shopping Cart:
        - After logging in, you will see a list of products.
        - Select any product by clicking on its **Add to cart** button.
    3. Go to the Shopping Cart:
        - Click on the shopping cart icon.
        - Verify that the selected product is displayed in the cart.
    4. Proceed to Checkout:
        - Click the **Checkout** button on the cart page.
    5. Fill in the Delivery Information:
        - On the **Checkout: Your Information** page, fill in the required fields:
          - First Name
          - Last Name
          - Postal Code
        - Click the **Continue** button.
    6. Confirm the Order:
        - Review the order details on the Checkout Overview page.
        - Click the **Finish** button to complete the purchase.
    7. Verify the final Confirmation Message:
        - After finishing, you should be redirected to the Checkout Complete page.
        - Verify that the text **"Thank you for your order!"** is displayed.

### Implement the Automation Script
- Use Python (`pytest` and `selenium`) to write your automation script.
- Organize your code with functions or classes for better readability and reusability.
- Use explicit waits (`WebDriverWait`) to handle dynamic content loading.
- Add assertions to validate each critical step.
- Optionally:
    - Modify your script to run on different browsers (Chrome, Firefox, etc.).
    - Use a data file (e.g., CSV or JSON) to input multiple sets of data.

> [!IMPORTANT]  
> Create a fork of this repository and provide a link to it when you are ready to deliver. If you already have a fork - use it to complete all tasks.
