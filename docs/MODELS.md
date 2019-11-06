# Estrutura da aplicação

Na figura abaixo, observamos a estrutura principal desta aplicação. De seguida serão apresentados em detalhe os pacotes constituíntes, e as suas respetivas funções.

``` sh
├── docs
│ ├── ABSTRACT.md
│ ├── INSTALATION.md
│ ├── MODELS.md
│ └── USEAPP.md
├── README.md
├── requirements.txt
├── run.py
└── ubiwhere_challenge
    ├── auth
    │ ├── __init__.py
    │ └── routes.py
    ├── errors
    │ ├── errors_handler.py
    │ ├── __init__.py
    ├── __init__.py
    ├── models.py
    ├── occurrences
    │ ├── __init__.py
    │ ├── routes.py
    │ └── utils.py  
```

## Ubiwhere Challenge
Nesta diretoria encontramos o pacote principal da aplicação.

### Autenticação
Todos os módulos associados à autenticação podem ser encontrados na diretoria "auth/".

Aqui, encontramos as funcionalidades de Registo, Login e Logout.

### Operações sobre as ocorrências
Para as operações sobre as ocorrências, foram separados os pacotes na diretoria "occurrences/". Este (pacote), é composto pela definição dos Endpoints, descritos e apresentados em [endpoints](USEAPP.md), e pelo ficheiro "utils.py", que contém funcões adicionais que foram implementadas.

### Modelos

No ficheiro "models.py", foram definidos os modelos de objetos a serem considerados nesta aplicação. Destacamos o modelo de User: 

``` python
class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    occurrences = db.relationship('Occurrence', backref='user', lazy=True)
```
E de Occurrence, respetivamente: 
``` python
class Occurrence(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(22), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Float, nullable=False)
```

A relação entre as entidades é de uma para muitas.
``` sh
User 1________*Occurrence
```