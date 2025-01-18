from loguru import logger

def generate_messages():
    messages = [
        "Custom Message 1: Example data",
        "Custom Message 2: Another data stream",
        "Custom Message 3: Special event detected!"
    ]
    for message in messages:
        logger.info(f"Generated message: {message}")
        yield message

# Example of using the generator
if __name__ == "__main__":
    for msg in generate_messages():
        pass
