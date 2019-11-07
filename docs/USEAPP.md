# Como usar a aplicação
Nesta seção são apresentados os diversos métodos para utilização da aplicação

### Postman Collection
https://www.getpostman.com/collections/aadea80379b033b62d2d

## Criar uma conta de Administrador de sistema

Antes de começar a utilizar a aplicação, o utilizador do sistema deve criar uma conta de utilizador. Tal é possível, realizando um request POST ao Endpoint: 
``` url
127.0.0.1:5000/register
```
De seguida é apresentado um exemplo desse pedido HTTP.
``` html
POST /register HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
cache-control: no-cache
Postman-Token: 91a303b1-b7ab-41a5-90df-a37fe25066bf

{
	"username": "admin",
	"name": "Admin",
	"email": "admin@admin.com",
	"password": "adminpass"
}
```

### Output esperado
```json
{"code": 200, "description": "The user was successful created"}
```

## Criar uma conta de Utilizador

Após criado um administrador de sistema, podem ser criadas contas de utilizador. Estas são utilizadas para associar a uma ocorrência. Tal é possível, realizando um request POST ao Endpoint: 
``` url
127.0.0.1:5000/register
```
De seguida é apresentado um exemplo desse pedido HTTP.

``` html
POST /register HTTP/1.1
Host: 127.0.0.1:5000
cache-control: no-cache
Postman-Token: 826bf70d-7423-4495-bd33-8dab0c0306eb

{
	"username": "user1",
	"name": "Utilizador 1",
	"email": "user1@mail.com",
	"password": "user1pass"
}
```
### Output esperado
```json
{"code": 200, "description": "The user was successful created"}
```

## Login de Administrador/ Utilizador

Um administrador ou utilizador pode fazer login no sistema. Isto garante que os posts realizados sejam autenticados. Tal é possível, realizando um request POST ao Endpoint: 
``` url
127.0.0.1:5000/login
```
De seguida é apresentado um exemplo desse pedido HTTP. Devem ser realizadas as alterações com as credênciais respetivas.
``` html
POST /login HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
cache-control: no-cache
Postman-Token: 899a217d-e70a-4273-ad81-3d623e0ad37b

{
	"email": "admin@admin.com",
	"password": "adminpass"
}
```

### Output esperado
```json
{"code": 200, "description": "The user was successful logged in"}
```

## Logout de Administrador/ Utilizador

De igual forma, o utilizador pode fazer logout do sistema. Tal é possível, realizando um request GET ao Endpoint: 
``` url
127.0.0.1:5000/logout
```
De seguida é apresentado um exemplo desse pedido HTTP. 
``` html
GET /logout HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
cache-control: no-cache
Postman-Token: ef348f9e-7f73-4c81-b2ab-3fa06a6ac1fb
```

### Output esperado
```json
{"sucess": "User logged out"}
```

## Criar uma nova ocorrência

Um utilizador pode inserir novas ocorrências no sistema. Tal é possível, realizando um request POST ao Endpoint: 
``` url
127.0.0.1:5000/occurrence
```
De seguida é apresentado um exemplo desse pedido HTTP. 
``` html
POST /occurrence/ HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
User-Agent: PostmanRuntime/7.19.0
Accept: */*
Cache-Control: no-cache
Postman-Token: c62d5bf8-6c23-442b-a76b-2711c3e0465e,5e61f3c2-1eca-40a3-a399-e936f3f6fe11
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate
Content-Length: 212
Cookie: session=.eJwlzjsOwjAMANC7eO4QO_EnvUyV2LFgbemEuDtITG99bzjyXNcD9td5rw2OZ8AOVqmReGvVK3twjtK7ZjVjz8QyialIth6pjjOXelqMLMVHl5EyhcxzkGLhaSpCzkhi0YN7KM2mlLxm1e6J_hO5YyzMsaYJbHBf6_xnKny-mfsvWw.XcK85g.Xjs6sJfuIfVlyPhwFITRbS_2QKA
Connection: keep-alive
cache-control: no-cache

{
        "description": "Ocorrência 1",
        "location": {
            "latitude" : 40.65593350,
            "longitude" : -8.441236878
        },
        "state": 0,
        "category": "CONSTRUCTION"
    }
```

### Output esperado
```json
{"code": 200, "description": "The occurrence was successful created"}
```

## Listar todas as ocorrências inseridas no sistema

Um utilizador pode listar todas as ocorrências no sistema. Tal é possível, realizando um request GET ao Endpoint: 
``` url
127.0.0.1:5000/occurrences
```

### Output esperado
```json
{
    "category": "CONSTRUCTION",
    "date_created": "2019-11-06T19:24:25.830767",
    "date_updated": "2019-11-06T19:24:25.830778",
    "description": "Ocorrência 1",
    "distance": 17.0967505363638,
    "id": 13,
    "latitude": 40.6559335,
    "longitude": -8.441236878,
    "state": 0,
    "user": 3
  }
```

## Listar todas as ocorrências por utilizador

Um utilizador pode inserir listar todas as ocorrências no sistema, filtradas por utilizador. Tal é possível, realizando um request GET ao Endpoint: 
``` url
127.0.0.1:5000/occurrences/author/id_user
```
O id_user é do tipo inteiro, e corresponde ao autor da ocorrência que se pretende filtrar.
### Output esperado
É esperado uma lista de ocorrências.

## Listar todas as ocorrências por categoria

Um utilizador pode inserir listar todas as ocorrências no sistema, filtradas por categoria. Tal é possível, realizando um request GET ao Endpoint: 
``` url
127.0.0.1:5000/occurrences/category/category
```
A category é do tipo string, e corresponde à categoria da ocorrência que se pretende filtrar. Esta pode tomar os valores de:
* CONSTRUCTION: planned road work
* SPECIAL_EVENT: special events (fair, sport event, etc.)
* INCIDENT: accidents and other unexpected events
* WEATHER_CONDITION: weather condition affecting the road
* ROAD_CONDITION: status of the road that might affect travellers (potholes, bad pavement, etc.)

### Output esperado
É esperado uma lista de ocorrências.

## Listar todas as ocorrências por distância

Um utilizador pode inserir listar todas as ocorrências no sistema, filtradas por distância. Ao ser inserida na base de dados, a distância da ocorrência é calculada desde o ponto dessa ocorrência até ao escritório da Ubiwhere. Tal é possível, realizando um request GET ao Endpoint: 
``` url
127.0.0.1:5000/occurrences/distance/distance
```
A distance é do tipo inteiro, e corresponde à distância da ocorrência que se pretende filtrar.

### Output esperado
É esperado uma lista de ocorrências.

## Realizar um update a uma ocorrência

Um administrador pode fazer um update a uma ocorrências no sistema. O update é feito ao estado da ocorrência. Tal é possível, realizando um request POST ao Endpoint: 

``` url
127.0.0.1:5000/occurrences/id_occurrence/update
```
O id_occurrence é do tipo inteiro, e corresponde ao id da ocorrência que se pretende realizar o update.

### Output esperado
``` json
{"code": 200, "description": "The occurrence was successful updated"}
```