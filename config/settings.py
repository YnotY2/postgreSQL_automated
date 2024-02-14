import os

# Database PostgreSQL Credentials
postgresql_db_name = os.getenv("postgresql_db_name","example_database")
postgresql_db_passwd = os.getenv("postgresql_db_passwd", "example_password")
postgresql_db_usr = os.getenv("postgresql_db_usr", "example_user")
postgresql_port = os.getenv("postgresql_port", "5432")
postgresql_host = os.getenv("postgresql_host", "localhost")
