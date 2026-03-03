from utils.logger import setup_logging
from core import processor

setup_logging()

if __name__ == '__main__':
    processor.process(10,0)