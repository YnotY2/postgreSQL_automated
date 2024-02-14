from utils.colors import Colors
from utils.logger import setup_logger

from services_python.start_postgresql import start_postgresql
from services_python.stop_postgresql import stop_postgresql
from services_python.check_status_postgresql_service import check_status_postgresql_service
from services_python.connect_db import connect_db
from services_python.quit_db_connection import quit_db_connection

# Setup logger with service name
service_name = "main"
logger = setup_logger(service_name)

def main():
    try:

        logger.info(f"{Colors.CYAN}Starting{Colors.END}{Colors.YELLOW} main.py{Colors.END} {Colors.CYAN} python3 script ...{Colors.END}")


        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} start_posgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        start_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} connect_db.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        cursor = connect_db()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} quit_db_connection.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        quit_db_connection(cursor)

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} stop_postgresql.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        stop_postgresql()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} check_status_postgresql_service.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        check_status_postgresql_service()



    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
