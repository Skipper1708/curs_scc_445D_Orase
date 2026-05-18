# README - Barcelona | Vlăsceanu Mihnea-Ștefan | 445D

## Cuprins

1. [Descriere functionalitate](#1-descriere-functionalitate)
2. [Stadiul implementarii](#2-stadiul-implementarii)
3. [Testare](#3-testare)
4. [Integrare Git](#4-integrare-git)
5. [Containerizare Docker](#5-containerizare-docker)
6. [Pull Request-uri reviewate](#6-pull-request-uri-reviewate)
7. [Ce mai este de facut](#7-ce-mai-este-de-facut)

---

## 1. Descriere functionalitate

**Element ales:** Barcelona (tema grupei: Orase)  
**Student:** Vlăsceanu Mihnea-Ștefan  
**Grupa:** 445D  

### Fisiere adaugate

| Fisier | Rol |
|--------|-----|
| `orase.py` | Aplicatia Flask principala |
| `app/lib/biblioteca_orase.py` | Functii specifice elementului Barcelona |
| `app/tests/test_lib_orase.py` | Unit-teste pentru functiile din librarie |
| `Dockerfile` | Containerizare aplicatie (FROM python:3.10-alpine) |
| `Jenkinsfile` | Pipeline CI/CD (Build, Calitate, Testare, Deploy) |

### Rute web disponibile

| Ruta | Descriere |
|------|-----------|
| `/` | Pagina principala cu butoane |
| `/orase` | Lista orase disponibile |
| `/barcelona` | Pagina dedicata Barcelonei |
| `/barcelona/populatie` | Afiseaza populatia Barcelonei |
| `/barcelona/descriere` | Afiseaza descrierea Barcelonei |

### Functii librarie (`biblioteca_orase.py`)

- **`populatie_barcelona()`** — returneaza un string cu informatii despre populatia Barcelonei (~1.636.000 locuitori)
- **`descriere_barcelona()`** — returneaza un string cu descrierea generala a Barcelonei (locatie, atractii, JO 1992)

---

## 2. Stadiul implementarii

- [x] Cod functional adaugat in `orase.py`
- [x] Librarie `app/lib/biblioteca_orase.py` creata cu 2 functii
- [x] Unit-teste scrise in `app/tests/test_lib_orase.py`
- [x] Dockerfile creat
- [x] Jenkinsfile creat (4 stagii: Build, Calitate Cod, Testare, Deploy)
- [x] Cod adaugat in branch `dev_vlasceanu_mihnea`
- [x] Pull Request creat catre `main_vlasceanu_mihnea`
- [x] README integrat in `main` prin Pull Request

---

## 3. Testare

### Testare manuala

Pornire aplicatie local:

```bash
# Clonare repository
git clone https://github.com/<user>/curs_scc_445D_orase.git
cd curs_scc_445D_orase

# Creare venv si instalare dependinte
python3 -m venv .venv
source .venv/bin/activate
pip install -r quickrequirements.txt

# Pornire server
export FLASK_APP=orase
flask run --host=0.0.0.0 --port=5011
```

Acces din browser: `http://localhost:5011`

### Testare cu pytest

```bash
source .venv/bin/activate
pytest app/tests/ -v
```

Rezultat asteptat:
```
app/tests/test_lib_orase.py::test_populatie_barcelona PASSED
app/tests/test_lib_orase.py::test_descriere_barcelona PASSED
2 passed in X.XXs
```

### Testare cu Jenkins

Pipeline Jenkins configurat cu 4 stagii:

1. **Build** — creaza mediu virtual Python (`.venv`) si instaleaza dependintele
2. **Calitate Cod** — ruleaza `pylint` pe `app/lib/*.py`, `app/tests/*.py`, `orase.py`
3. **Testare** — ruleaza `pytest app/tests/ -v`
4. **Deploy** — construieste imaginea Docker si porneste containerul pe portul 5011

**Rezultat Jenkins:** PASS ✓

> _[Adauga screenshot cu build Jenkins reusit]_

---

## 4. Integrare Git

### Structura branch-uri

```
main (protejat)
├── main_vlasceanu_mihnea
│   └── ← PR din dev_vlasceanu_mihnea (cu review)
└── dev_vlasceanu_mihnea  ← codul personal
```

### Workflow utilizat

```bash
# Pe VM, clonare si setup initial
git clone https://github.com/<user>/curs_scc_445D_orase.git
cd curs_scc_445D_orase

# Creare branch-uri personale
git checkout -b main_vlasceanu_mihnea
git push -u origin main_vlasceanu_mihnea

git checkout -b dev_vlasceanu_mihnea
git push -u origin dev_vlasceanu_mihnea

# Lucru pe dev, commit si push
git add .
git commit -m "Adaugare functionalitate Barcelona"
git push origin dev_vlasceanu_mihnea

# Pull Request: dev_vlasceanu_mihnea -> main_vlasceanu_mihnea
# (creat pe GitHub, cu minim 1 reviewer)
```

**Status integrare:** README integrat in `main` prin Pull Request cu review aprobat ✓

---

## 5. Containerizare Docker

### Construire imagine

```bash
docker build -t orase_barcelona:latest .
```

### Pornire container

```bash
docker run -d --name orase_container -p 5011:5011 orase_barcelona:latest
```

### Verificare

```bash
# Verificare container activ
docker ps

# Acces aplicatie din browser
# http://localhost:5011
```

### Capturi de ecran

> _[Adauga screenshot: imagine Docker creata - `docker images`]_  
> _[Adauga screenshot: container pornit - `docker ps`]_  
> _[Adauga screenshot: browser acceseaza `http://localhost:5011/barcelona`]_  
> _[Adauga screenshot: log-uri container - `docker logs orase_container`]_

---

## 6. Pull Request-uri reviewate

| PR ID | Autor | Element | Status review |
|-------|-------|---------|--------------|
| #XX | Coleg 1 | Bucuresti | Aprobat |
| #XX | Coleg 2 | Paris | Aprobat |

> _[Completeaza cu ID-urile reale dupa ce colegii deschid PR-urile]_

---

## 7. Ce mai este de facut

- [ ] Adaugare capturi de ecran Docker in README
- [ ] Adaugare capturi de ecran Jenkins in README
- [ ] Completare tabel Pull Request-uri reviewate
- [ ] (Optional) Push imagine pe DockerHub
