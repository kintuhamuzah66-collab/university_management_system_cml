import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

from cli.interface import menu 

if __name__ == "__main__":
    try:
        logger.info("main started!")
        menu()
        logger.info("main stopped")
    except Exception:
        logger.exception("Something went wrong")