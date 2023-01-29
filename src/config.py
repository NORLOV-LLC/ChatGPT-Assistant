
import os
import dotenv
import logging
import time
from pathlib import Path


logging.basicConfig(
    format='%(asctime)s [%(levelname)-8.8s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%SZ',
    level=logging.INFO
)
logging.Formatter.converter = time.gmtime

PRJ_DIR: Path = Path(__file__).parent.parent
# print(PRJ_DIR)

DATA_DIR: Path = PRJ_DIR.joinpath('data')
CONFIG_DIR: Path = PRJ_DIR.joinpath('config')


env_file = os.getenv('CA_ENV', '').lower().strip()
if not env_file:
    msg = f"Missing OS env var `CA_ENV`"
    logging.error(msg)
    raise ValueError(msg)

file_name = f"{env_file}.env"
file_path = CONFIG_DIR.joinpath(file_name)
logging.info(f"Loading config ca_env={env_file} from {file_path}")
if not file_path.exists():
    msg = f"Env file not found: {file_path}"
    logging.error(msg)
    raise FileNotFoundError(msg)
# OS env > .env
dotenv.load_dotenv(str(file_path))
