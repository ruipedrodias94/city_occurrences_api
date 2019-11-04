# Ubiwhere Challenge

### Developed by Rui Pedro Dias

## Abstract
Pretende-se uma API REST que permita a gestão de ocorrências em ambiente urbano. As ocorrências devem ter descrição, uma localização geográfica, autor, data de criação, data de actualização, estado (por validar, validado, resolvido) e uma das seguintes categorias:

CONSTRUCTION: planned road work
SPECIAL_EVENT: special events (fair, sport event, etc.)
INCIDENT: accidents and other unexpected events
WEATHER_CONDITION: weather condition affecting the road
ROAD_CONDITION: status of the road that might affect travellers (potholes, bad pavement, etc.)

## Requisitos
1) API REST
1.1) Tem de permitir a adição de ocorrências (com a localização geográfica, e autor associados). Nota: O estado default será sempre por validar quando estas são criadas. -> DONE
1.2) Tem de permitir a actualização de ocorrências (para mudar o estado das mesmas para "validadas" por um administrador do sistema) - DONE
1.3) Tem de permitir a filtragem de ocorrências por autor, por categoria e por localização (raio de alcance)

## Notas sobre o exercício
A) A componente da API REST deve ser desenvolvida Flask ou Falcon. É obrigatória a partilha de uma collection Postman para conseguirmos testar rapidamente os endpoints que implementares.
B) A BD deixamos ao teu critério (SQLite, PostgresQL, MySQL,…) - mas recomendamos PostgreSQL com PostGIS para a parte geográfica.
C) Serás também valorizado caso coloques o código implementado no Github.

