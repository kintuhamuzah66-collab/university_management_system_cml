import logging
from classes.registrar import AcademicRegistrar

# 1. Setup logging configuration ONCE at the entry point
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(),  # Print to console
        logging.FileHandler("project.log"),  # Save to file
    ],
)

# Create a logger for the main file too, if you want
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting the application...")

    # Initialize your manager and run your code
    mgr = AcademicRegistrar("Kintu", "Hamza")
    mgr.remove_departement("HR")

    logger.info("Application finished.")


if __name__ == "__main__":
    main()