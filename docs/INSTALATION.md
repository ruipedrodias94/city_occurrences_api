# INSTALAÇÃO

Nesta secção vão ser apresentados os passos a replicar para poder instalar esta aplicação

### Fazer git clone do repositório em causa

```sh
$ git clone https://github.com/ruipedrodias94/ubiwhere_challenge
```

### Instalar e criar um ambiente virtual
```sh
$  pip install virtualenv
$  virtualenv env
```

### Activar o ambiente e instalar as dependências
```sh
$  source bin/env/activate
$  pip install -r requirements.txt 
```
## Montar a base de dados localmente

```sh
$  python
```

```python
from ubiwhere_challenge import db
from ubiwhere_challenge.models import User, Occurrence
db.create_all()
```

### A base de dados pode também ser acedida remotamente, para isso é necessário descomentar a linha com a configuração da mesma, no ficheiro "ubiwhere\_challenge"/\_\_init\_\_.py"

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost/local_database"
```

## De seguida podemos executar a aplicação
```sh
$  python run.py
```