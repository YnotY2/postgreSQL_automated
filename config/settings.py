import os

# Database PostgreSQL Credentials
postgresql_db_name = os.getenv("postgresql_db_name","yahoo_mail_sender")
postgresql_db_passwd = os.getenv("postgresql_db_passwd", "G6OhE/mnoW_D!Ss/ocN")
postgresql_db_usr = os.getenv("postgresql_db_usr", "yahoo_mail_sender")
postgresql_port = os.getenv("postgresql_port", "5432")
postgresql_host = os.getenv("postgresql_host", "localhost")
