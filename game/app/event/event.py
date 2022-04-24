"""Работа с событиями"""

from base.provider import Provider

__author__ = 'Чусовитин А.Р.'


class Event:

    def __init__(self):
        self.db = Provider('./event/sql')

    def insert_event(self, parameters):
        self.db.exec_by_file('insert_event.sql', parameters)
