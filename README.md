# Urmuz Laurentiu - grupa 445D

## Cuprins
1. Scopul proiectului
2. Date generale
3. Structura proiectului
4. Functionalitatea implementata
5. Descrierea fisierelor
6. Testare locala
7. Integrare Git si GitHub
8. Jenkins
9. Containerizare Docker
10. Pull Request-uri si review

## Scopul proiectului
Acest proiect a fost realizat in cadrul disciplinei Servicii Cloud si Containerizare si urmareste folosirea practica a tehnologiilor: masina virtuala, Git si GitHub, Jenkins, Docker si Flask. Am ales orasul Viena pentru tema Orase a grupei 445D.

## Date generale
- Nume: Urmuz Laurentiu Ioan
- Grupa: 445D
- Tema: Orase
- Element ales: Viena
- Repository: curs_scc_445D_Orase
- Branch dezvoltare: dev_Urmuz_Laurentiu
- Branch principal: main_Urmuz_Laurentiu
## Functionalitatea implementata
Aplicatia ofera:
- pagina principala
- pagina pentru tema Orase
- pagina dedicata orasului Viena
- pagina pentru populatia Vienei
- pagina pentru descrierea Vienei

## Descrierea fisierelor

**orase.py** - fisierul principal Flask cu rutele: `/`, `/orase`, `/viena`, `/populatie_viena`, `/descriere_viena`

**app/lib/biblioteca_orase.py** - contine functiile:
- `populatie_viena()` - returneaza populatia orasului Viena
- `descriere_viena()` - returneaza o descriere a orasului Viena

**app/tests/test_biblioteca_orase.py** - 4 teste automate pentru cele doua functii

**Dockerfile** - containerizarea aplicatiei cu FROM alpine, port 5011

**Jenkinsfile** - pipeline cu etapele: Build, Test, Deploy

## Testare locala
```bash
# Rulare aplicatie
python3 orase.py

# Rulare teste
pytest app/tests/ -v
```

Rute verificate:
- http://127.0.0.1:5011/
- http://127.0.0.1:5011/orase
- http://127.0.0.1:5011/viena
- http://127.0.0.1:5011/populatie_viena
- http://127.0.0.1:5011/descriere_viena

## Integrare Git si GitHub
- clonare repository de grupa
- lucru pe branch-ul dev_Urmuz_Laurentiu
- commit si push fisiere
- creare Pull Request din dev_Urmuz_Laurentiu catre main_Urmuz_Laurentiu
- obtinere review de la coleg

## Jenkins
Pipeline cu etapele:
- Build - construire imagine Docker
- Test - rulare pytest
- Deploy - pornire container

## Containerizare Docker
```bash
docker build -t orase_viena_urmuz .
docker run -d --name container_viena -p 8020:5011 orase_viena_urmuz
```
Acces din browser: http://127.0.0.1:8020
## Screenshots


### Docker logs
<img width="975" height="691" alt="image" src="https://github.com/user-attachments/assets/51f4e00c-8fa7-495f-bbfa-102b3fecc929" />

### Teste pytest - PASSED
<img width="975" height="633" alt="image" src="https://github.com/user-attachments/assets/065ce8c6-0479-465e-ac36-801b07b6cc30" />

### Docker container running
<img width="975" height="362" alt="image" src="https://github.com/user-attachments/assets/0a6d98ec-9794-432f-94ab-662a543c7296" />


### Aplicatie in browser din container
<img width="975" height="690" alt="image" src="https://github.com/user-attachments/assets/90c53ee4-e520-4cfd-aac6-d50389ec6dd8" />

### Jenkins - Configurare
<img width="975" height="628" alt="image" src="https://github.com/user-attachments/assets/abf3b295-1599-4668-b51b-d4d01f865190" />

### Jenkins Pipeline - SUCCESS
<img width="975" height="530" alt="image" src="https://github.com/user-attachments/assets/70e9fd71-be7b-4b65-b1c1-17f7a5346579" />

### Docker images
<img width="975" height="628" alt="image" src="https://github.com/user-attachments/assets/46263055-8c02-4114-aff4-53c88f3bb248" />

### Docker logs
<img width="975" height="384" alt="image" src="https://github.com/user-attachments/assets/06f8d018-7982-4211-ac14-24d2e1bce000" />


## Pull Request-uri si review
- PR creat: dev_Urmuz_Laurentiu → main_Urmuz_Laurentiu
- Review: in asteptare
- Status: in lucru 
