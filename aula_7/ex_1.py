
import datetime

import sqlalchemy


engine = sqlalchemy.create_engine(
    'sqlite:///app.db',
    echo=True
)

metadata = sqlalchemy.MetaData(bind=engine)

users_table = sqlalchemy.Table(
    'tb_users',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),
    sqlalchemy.Column(
        'name',
        sqlalchemy.String(50),
        index=True
    ),
    sqlalchemy.Column(
        'age',
        sqlalchemy.Integer,
        nullable=False
    ),
    sqlalchemy.Column(
        'password',
        sqlalchemy.String        
    ),
    sqlalchemy.Column(
        'created_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    ),
    sqlalchemy.Column(
        'updated_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )
)

addrs_table = sqlalchemy.Table(
    'tb_addresses',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),
    sqlalchemy.Column(
        'name',
        sqlalchemy.String,
        nullable=False
    )
)

if __name__ == '__main__':
    metadata.create_all(engine)