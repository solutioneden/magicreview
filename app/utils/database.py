from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConnection:
    def __init__(self):
        self.ssh_host = os.getenv("SSH_HOST")
        self.ssh_port = int(os.getenv("SSH_PORT"))
        self.ssh_user = os.getenv("SSH_USERNAME")
        self.ssh_password = os.getenv("SSH_PASSWORD")
        self.ssh_private_key = os.getenv("SSH_PRIVATE_KEY")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = int(os.getenv("DB_PORT"))
        self.db_user = os.getenv("DB_USERNAME")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")

    def __enter__(self) -> Engine:
        self.server = SSHTunnelForwarder(
            (self.ssh_host, self.ssh_port),
            ssh_username=self.ssh_user,
            ssh_pkey=self.ssh_private_key,
            remote_bind_address=(self.db_host, self.db_port),
        )
        self.server.start()
        local_port = self.server.local_bind_port
        self.engine = create_engine(
            f"mysql+pymysql://{self.db_user}:{self.db_password}@127.0.0.1:{local_port}/{self.db_name}"
        )
        return self.engine

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.dispose()
        self.server.stop()
