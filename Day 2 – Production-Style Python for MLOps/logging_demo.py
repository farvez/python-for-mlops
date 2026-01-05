import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("pipeline started")
logging.warning("low accuracy detected")
logging.error("Training failed")