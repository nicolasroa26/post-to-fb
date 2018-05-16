from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Sequence
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
import sqlalchemy

engine = create_engine('postgres://fhpebriezsuyly:576364a25eed0956440777de9005f84bd021b89d5f65817338be42fc19df35de@ec2-23-23-180-121.compute-1.amazonaws.com:5432/d6b8r5d8bu18ri', echo=True)
metadata = MetaData()
formulario = Table('formulario', metadata,
    Column('id', Integer, primary_key=True),
    Column('post', String),
    Column('tokens', String),
    Column('groups', String),
    Column('notification', String)
)
metadata.create_all(engine)

def insert(groups, usuarios, message):
	connection = engine.connect()
	ins = formulario.insert().values(post=message, tokens=str(usuarios), groups=groups, notification='Done')
	ins.compile().params
	result = connection.execute(ins)
	ins.bind = engine
	result.inserted_primary_key

def table():
	s = select([formulario])
	connection = engine .connect()
	result = connection.execute("select * from formulario")
	return result