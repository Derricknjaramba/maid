class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # SQLite for local dev, change for production
    SECRET_KEY = 'your_secret_key'  # Replace with a secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables unnecessary overhead for each modification









