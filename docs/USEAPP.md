# Como usar a aplicação
Nesta seção são apresentados os diversos métodos para utilização da aplicação

## Criar uma conta de Administrador de sistema

Antes de começar a utilizar a aplicação, o utilizador do sistema deve criar uma conta de utilizador. Tal é possível, realizando um request POST ao Endpoint: 
``` url
127.0.0.1:5000/register
```
De seguida é apresentado um exemplo desse pedido HTML.
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
De seguida é apresentado um exemplo desse pedido HTML.

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
De seguida é apresentado um exemplo desse pedido HTML. Devem ser realizadas as alterações com as credênciais respetivas.
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

De igual forma, o utilizador pode fazer logout do sistema. Tal é possível, realizando um request POST ao Endpoint: 
``` url
127.0.0.1:5000/logout
```
De seguida é apresentado um exemplo desse pedido HTML. 
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