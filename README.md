# PostgreSQL Service Integration in Python3

This repository serves as a reminder of the necessary files and helpful functions when using PostgreSQL service within Python3 code. It provides a structured approach for integrating PostgreSQL into your Python projects efficiently.
The layout is exacly what you need, it's very clean and logical. If you want to connect to a newly created database. Simply navigate to "conig/settings.py" config module for setting up a credentials for the actuall corresponding datbase.
Here is the actuall "settings.py"-file: 

```python
import os

# Database PostgreSQL Credentials
postgresql_db_name = os.getenv("postgresql_db_name","example_database")
postgresql_db_passwd = os.getenv("postgresql_db_passwd", "example_password")
postgresql_db_usr = os.getenv("postgresql_db_usr", "example_user")
postgresql_port = os.getenv("postgresql_port", "5432")
postgresql_host = os.getenv("postgresql_host", "localhost")
```


## Files Included:

- **main.py**: The main Python script responsible for orchestrating the PostgreSQL service integration.
- **utils/colors.py**: A utility module for defining color constants used in logging messages.
- **utils/logger.py**: A utility module for setting up a logger with a specified service name.
- **conig/settings.py**: A config module for setting up a credentials for the actuall corresponding datbase.
- **services_python/start_postgresql.py**: Python script to start the PostgreSQL service.
- **services_python/connect_db.py**: Python script to establish a connection to the PostgreSQL database.
- **services_python/quit_db_connection.py**: Python script to gracefully close the PostgreSQL database connection.
- **services_python/stop_postgresql.py**: Python script to stop the PostgreSQL service.
- **services_python/check_status_postgresql_service.py**: Python script to check the status of the PostgreSQL service.
- **services_sh/start_posgresql.sh.sh**: SH script to check the status of the PostgreSQL service. (called by python3 code)
- **services_sh/stop_postgresql.sh.sh**: SH script to check the status of the PostgreSQL service. (called by python3 code)
- **services_sh/check_status_postgresql_service.sh**: SH script to check the status of the PostgreSQL service. (called by python3 code)


## Usage:

1. **Setup Logger**: Use the `setup_logger()` function from `utils/logger.py` to set up a logger with a specified service name.
2. **Main Script Execution**: Execute `main.py` to integrate PostgreSQL service into your Python project.
3. **Function Calls**:
   - `start_postgresql()`: Call this function to start the PostgreSQL service.
   - `connect_db()`: Call this function to establish a connection to the PostgreSQL database.
   - `quit_db_connection(cursor)`: Call this function to gracefully close the PostgreSQL database connection.
   - `stop_postgresql()`: Call this function to stop the PostgreSQL service.
   - `check_status_postgresql_service()`: Call this function to check the status of the PostgreSQL service.
4. **Error Handling**: Exception handling is implemented to catch and log errors encountered during script execution.
5. **Pull Request**: You can easily create a GitHub pull request for this repository when starting a new project to include PostgreSQL service integration.


## :D 
