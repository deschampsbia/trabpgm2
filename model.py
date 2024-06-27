from config import *

class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)
    def __str__(self):
        return f'{self.nome}, {self.email}, {self.telefone}'

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)