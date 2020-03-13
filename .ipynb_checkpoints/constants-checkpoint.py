from dotenv import load_dotenv
from pyathena import connect
import os

# define project location
PROJ_DIR: str = os.path.dirname(os.path.abspath(__file__))

# load local environment variables
env_name: str = ".env"
load_dotenv(dotenv_path=os.path.join(PROJ_DIR, env_name))

def get_conn():
    """Allow lazily calling of pyathena connection."""
    return connect(aws_access_key_id=os.getenv("ACCESS_KEY"),
                   aws_secret_access_key=os.getenv("SECRET_KEY"),
                   s3_staging_dir=os.getenv("S3_DIR"),
                   region_name=os.getenv("REGION_NAME"))