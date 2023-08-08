from pydantic import BaseSettings

class Settings(BaseSettings): 
   MYSQL_INITDB_URL: str = "mysql+pymysql://root:password123@localhost:3306/courses_db"

settings = Settings() 
    