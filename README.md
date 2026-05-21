# Varsovia — Ioana Delia | SCC 445D

## 1. Funcționalitatea adăugată

Aplicație Flask pentru orașul **Varsovia** (Polonia).

Funcții implementate în `app/lib/biblioteca_orase.py`:
- `populatie_varsovia()` — returnează populația orașului
- `descriere_varsovia()` — returnează o descriere a orașului

Rute disponibile:
| Rută | Descriere |
|------|-----------|
| `/` | Pagina principală |
| `/orase` | Lista orașelor disponibile |
| `/varsovia` | Pagina dedicată Varsoviei |
| `/varsovia/populatie` | Populația Varsoviei |
| `/varsovia/descriere` | Descrierea Varsoviei |

---

## 2. Stadiul implementării

- [x] `orase.py` — aplicație Flask cu 5 rute
- [x] `app/lib/biblioteca_orase.py` — cele 2 funcții
- [x] `app/tests/test_lib_orase.py` — teste pytest
- [x] `Dockerfile` — containerizare
- [x] `Jenkinsfile` — pipeline 4 stage-uri
- [x] `dockerstart.sh`, `activeaza_venv`, `activeaza_venv_jenkins`
- [x] `pytest.ini`, `quickrequirements.txt`
- [ ] Screenshots Jenkins PASS
- [ ] Screenshots Docker

---

## 3. Testare

### Rulare locală Flask
```bash
. ./activeaza_venv
flask run --port=5011
```

### Rulare teste pytest
```bash
. ./activeaza_venv
pytest app/tests/ -v
```

### Rulare Jenkins
1. Pe VM, `git pull` pe branch-ul `dev_Ioana_Delia`
2. Deschide Jenkins → pipeline-ul proiectului
3. Click **Build Now**
4. Verifică că toate 4 stage-uri sunt verzi (PASS)

*(screenshot Jenkins PASS — de adăugat după rulare pe VM)*

---

## 4. Integrare Git

Branch-uri:
- `dev_Ioana_Delia` — dezvoltare (branch curent)
- `main_Ioana_Delia` — versiune finalizată

Workflow:
```
dev_Ioana_Delia → main_Ioana_Delia  (PR cu review)
dev_Ioana_Delia → main              (doar README, PR cu review)
```

Status PR: în așteptare

---

## 5. Containerizare Docker

```bash
docker build -t orase_varsovia:latest .
docker stop orase_container || true
docker rm orase_container || true
docker run -d --name orase_container -p 5011:5011 orase_varsovia:latest
```

Screenshots de adăugat după rulare pe VM:
1. `docker images` — imaginea creată
2. `docker ps` — containerul pornit
3. Browser — aplicație accesată din container
4. `docker logs orase_container` — loguri

---

## 6. PR-uri la care am făcut review

| PR | Autor |
|----|-------|
| — | — |

*(de completat)*

---

## 7. Ce mai este de făcut

- Rulat Jenkins pe VM și adăugat screenshot PASS
- Rulat Docker pe VM și adăugat cele 4 screenshots
- Făcut review la minim 1 coleg
- Deschis PR `dev_Ioana_Delia` → `main_Ioana_Delia`
- Deschis PR cu README către `main`
