from concurrent.futures  import ThreadPoolExecutor, as_completed
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(threadName)s: - %(message)s')

logger = logging.getLogger(__name__)
from core.processor import process

def process_data(item):
    logger.debug(f"Processing item: {item}")
    result = 100 / item
    return result


def main():
    data = [10, 20, 30, 40 , 0]
    tuple_data =[(20, 10), (10, 5), (200, 5), (100,0 )]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures_to_item = {executor.submit(process_data, item): item for item in data}

        for future in as_completed(futures_to_item):
            item = futures_to_item[future]
            try:
                result = future.result()
                logger.info(f"success 100/ {item} = {result}")
            except ZeroDivisionError:
                logger.error(f"Failed: Item {item} caused a Division by zero")
            except Exception as e:
                logger.error(f"Unexpected error for item {item}: {e}")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures_to_item = {executor.submit(process, a, b): (a,b) for (a, b) in tuple_data}

        for future in as_completed(futures_to_item):
            a, b = futures_to_item[future]
            try:
                result = future.result()
                logger.info(f"success {a}/{b} = {result}")
            except ZeroDivisionError:
                logger.error(f"Failed: Item {a, b} caused a Division by zero")
            except Exception as e:
                logger.error(f"Unexpected error for item {a, b}: {e}")


if __name__ == '__main__':
    main()