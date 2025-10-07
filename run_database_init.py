import yaml
from sqlalchemy import create_engine
from retrieval_service.models import models

# Load configuration from YAML
with open("retrieval_service/config.yml", "r") as f:
    cfg = yaml.safe_load(f)

# Build the PostgreSQL connection URL (use port from datastore)
db_url = (
    f"postgresql://{cfg['datastore']['user']}:"
    f"{cfg['datastore']['password']}@"
    f"{cfg['datastore']['host']}:"
    f"{cfg['datastore'].get('port', 5432)}/"
    f"{cfg['datastore']['database']}"
)

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create all tables defined in models.py
models.Base.metadata.create_all(engine)

print("Database initialized successfully!")
