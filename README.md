Voting System API

API REST para gestionar un sistema de votaciones 

1. instalar dependecias usando 
pip install -r requirements.txt

2.crear la base de datos ejecutando el sql que se encuentra en votaciones/db

3.agregar en .../codigo/votacion/.env el usuario contraseña y puerto para la base de datos

4.para correr el programa desde .../codigo/votaciones en la terminal se usa uvicorn main:app --reload   

5.abrir http://127.0.0.1:8000/docs

Ejemplos
Post votantes
<img width="1427" height="692" alt="image" src="https://github.com/user-attachments/assets/86234c5d-2065-41b4-ba6c-59ca4d76e9ea" />
<img width="1405" height="598" alt="image" src="https://github.com/user-attachments/assets/7043f7cc-c3bc-4290-a6b4-08d447d65c6d" />

Delete votantes
<img width="1419" height="760" alt="image" src="https://github.com/user-attachments/assets/49184f10-8f76-4d38-8192-5eb4d2b2cb03" />

Get cantidatos
<img width="1413" height="831" alt="image" src="https://github.com/user-attachments/assets/c0717853-de27-448b-8c6f-c5ea8889faa1" />

post canditos 
<img width="1423" height="664" alt="image" src="https://github.com/user-attachments/assets/5b7f0dc3-7f41-4b7d-a20a-36a6cc60db78" />
<img width="1409" height="568" alt="image" src="https://github.com/user-attachments/assets/734a6520-f87d-4d2b-9aff-0ed3f4aee113" />

Post votos
<img width="1417" height="593" alt="image" src="https://github.com/user-attachments/assets/9b796327-0045-4212-9aff-fc7d17bf322c" />
<img width="1413" height="686" alt="image" src="https://github.com/user-attachments/assets/11f3bd97-8bc1-47f3-99d1-dd699ddbd523" />

Get estadisticas de los votos
<img width="1400" height="949" alt="image" src="https://github.com/user-attachments/assets/7a14a180-8433-46c0-b150-325824753723" />

al usar este ultimo se genera una imagen en .../codigo/votaciones/reports con la grafica
<img width="652" height="490" alt="image" src="https://github.com/user-attachments/assets/00d5db0b-60f4-494f-9471-bf5aaac547ee" />
