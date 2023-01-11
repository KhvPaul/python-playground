import os

from dotenv import load_dotenv

print("Calling load_dotenv func in example_package/config.py")
load_dotenv()

EXAMPLE_VARIABLE1 = os.getenv("EXAMPLE_VARIABLE1")
EXAMPLE_VARIABLE2 = os.getenv("EXAMPLE_VARIABLE2")
