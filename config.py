class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/mwh_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'