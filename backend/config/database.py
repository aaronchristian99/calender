from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

# Load environment variables
load_dotenv()

# Read database connection
DB_CONNECTION = getenv('DB_CONNECTION', 'mysql').lower()

# Define database URLs based on DB_TYPE
if DB_CONNECTION == "postgres":
    DB_URL = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
elif DB_CONNECTION == "mysql":
    DB_URL = f"mysql+mysqlconnector://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
elif DB_CONNECTION == "mssql":
    DB_URL = f"mssql+pyodbc://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}?driver=ODBC+Driver+17+for+SQL+Server"
elif DB_CONNECTION == "sqlite":
    DB_URL = f"sqlite:///{getenv('SQLITE_PATH')}"
else:
    raise ValueError("Unsupported DB_TYPE. Choose from 'postgres', 'mysql', 'mssql', or 'sqlite'.")

print(f'db url: {DB_URL}')

# Creating database engine
engine = create_engine(DB_URL, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models.User import User
    from models.Event import Event
    from models.PublicEvent import PublicEvent
    from models.PrivateEvent import PrivateEvent
    from models.CollaboratedEvent import CollaboratedEvent
    Base.metadata.create_all(bind=engine)