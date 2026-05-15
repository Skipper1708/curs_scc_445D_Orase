# Lisabona - Proiect SCC

## Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
2. [Structura proiect](#structura-proiect)
3. [Configurare si rulare](#configurare-si-rulare)
4. [Testare](#testare)
5. [Docker](#docker)
6. [Jenkins](#jenkins)

## Descriere aplicatie
Aplicatie Flask care afiseaza informatii despre orasul Lisabona.
Afiseaza populatia si o descriere a orasului.

## Structura proiect
curs_scc_445D_Orase/
├── app/
│   ├── lib/
│   │   └── biblioteca_orase.py
│   └── teste/
│       └── test_lisabona.py
├── orase.py
├── Dockerfile
├── Jenkinsfile
├── pytest.ini
├── quickrequirements.txt
└── README_lisabona.md
## Configurare si rulare
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r quickrequirements.txt
python3 orase.py
```
Acces aplicatie: http://127.0.0.1:5011

## Testare
```bash
pytest
```

## Docker
```bash
docker build -t orase-lisabona .
docker run -p 5011:5011 orase-lisabona
```

## Jenkins
Pipeline cu 3 etape: Build, Testare (pylint + pytest), Deploy (Docker).
