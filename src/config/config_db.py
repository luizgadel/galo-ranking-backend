import os
from src.config.environment_config import Environment

Environment.config_environment("localhost")

IP_HOST = os.environ["IP_HOST"]
PORT_HOST = os.environ["PORT_HOST"]

origins=["*"]