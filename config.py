import PySimpleGUI as sg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///taskprogram.db')
session = sessionmaker(bind=engine)()