import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

openai_api_key = os.getenv("OPENAI_API_KEY")
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
magicreview_api_review = os.getenv("MAGICREVIEW_API_REVIEW")
magicreview_api_key = os.getenv("MAGICREVIEW_API_KEY")



class Config:
    # SQLALCHEMY_DATABASE_URI = (
    #     f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    # )
    # SQLALCHEMY_DATABASE_ENGINE = create_engine(SQLALCHEMY_DATABASE_URI)
    OPENAI_API_KEY = openai_api_key
    LANGSMITH_API_KEY = langsmith_api_key
    MAGICREVIEW_API_REVIEW = magicreview_api_review
    MAGICREVIEW_API_KEY = magicreview_api_key
    
