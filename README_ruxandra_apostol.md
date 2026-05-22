# Proiect SCC - Orașe - Reykjavik
## Ruxandra Apostol - grupa 445D

---

## Cuprins

1. [Scopul proiectului](#scopul-proiectului)
2. [Date generale](#date-generale)
3. [Structura proiectului](#structura-proiectului)
4. [Funcționalitatea implementată](#funcționalitatea-implementată)
5. [Descrierea fișierelor](#descrierea-fișierelor)
6. [Funcții implementate](#funcții-implementate)
7. [Rute implementate](#rute-implementate)
8. [Testare](#testare)
9. [Jenkins](#jenkins)
10. [Docker](#docker)
11. [Git și GitHub](#git-și-github)
12. [Pull Request-uri și review](#pull-request-uri-și-review)
13. [Stadiul implementării](#stadiul-implementării)
14. [Ce mai este de făcut](#ce-mai-este-de-făcut)
15. [Capturi de ecran](#capturi-de-ecran)
16. [Concluzie](#concluzie)

---

## Scopul proiectului

Acest proiect a fost realizat în cadrul disciplinei **Servicii Cloud și Containerizare**.

Scopul proiectului este folosirea practică a unor unelte întâlnite în dezvoltarea software și DevOps:

- Git și GitHub
- Jenkins
- Docker
- Flask
- pytest
- pylint
- mașină virtuală Ubuntu

Tema grupei 445D este **Orașe**, iar elementul implementat de mine este orașul **Reykjavik**.

---

## Date generale

- **Student:** Ruxandra Apostol
- **Grupă:** 445D
- **Temă:** Orașe
- **Oraș ales:** Reykjavik
- **Repository:** `curs_scc_445D_Orase`
- **Branch de dezvoltare:** `dev_ruxandra_apostol`
- **Branch principal personal:** `main_ruxandra_apostol`
- **Fișier principal aplicație:** `orase.py`
- **Bibliotecă:** `app/lib/biblioteca_orase.py`
- **Port local aplicație:** `5000`
- **Port container Docker:** `5011`

---

## Structura proiectului

```text
.
├── app
│   ├── __init__.py
│   ├── lib
│   │   ├── __init__.py
│   │   └── biblioteca_orase.py
│   └── tests
│       └── test_orase.py
├── docs
│   └── imagini
│       ├── browser_reykjavik.png
│       ├── docker_images.png
│       ├── docker_logs.png
│       ├── docker_ps_a.png
│       ├── jenkins_build_success.png
│       └── jenkins_console_output.png
├── activeaza_venv
├── activeaza_venv_jenkins
├── dockerstart.sh
├── Dockerfile
├── Jenkinsfile
├── orase.py
├── pytest.ini
├── quickrequirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Funcționalitatea implementată

Am implementat o aplicație web Flask pentru tema **Orașe**, având ca element ales orașul **Reykjavik**.

Aplicația oferă:

- o pagină principală;
- o pagină pentru tema Orașe;
- o pagină dedicată orașului Reykjavik;
- o pagină pentru populația orașului Reykjavik;
- o pagină pentru descrierea orașului Reykjavik.

Interfața este realizată direct în Flask, folosind HTML și CSS incluse în paginile returnate de aplicație.

---

## Descrierea fișierelor

### `orase.py`

Este fișierul principal al aplicației Flask.

Conține:

- inițializarea aplicației Flask;
- funcția `pagina_html(...)`, folosită pentru generarea paginilor;
- rutele aplicației;
- stilizarea paginilor;
- pornirea aplicației local pe portul `5000`.

### `app/lib/biblioteca_orase.py`

Conține cele două funcții specifice orașului Reykjavik:

- `populatie_reykjavik()`
- `descriere_reykjavik()`

Aceste funcții returnează texte care sunt afișate în paginile aplicației.

### `app/tests/test_orase.py`

Conține testele automate pentru:

- funcțiile din bibliotecă;
- rutele Flask;
- răspunsurile HTTP ale aplicației.

### `pytest.ini`

Configurează rularea testelor cu `pytest`.

### `quickrequirements.txt`

Conține dependențele necesare proiectului:

```text
flask
pytest
pylint
gunicorn
```

### `Dockerfile`

Definește imaginea Docker a aplicației.

Imaginea folosită este:

```dockerfile
FROM python:3.10-alpine
```

### `dockerstart.sh`

Script folosit pentru pornirea aplicației Flask în container pe portul `5011`.

### `activeaza_venv`

Script pentru crearea și activarea mediului virtual local.

### `activeaza_venv_jenkins`

Script folosit în Jenkins pentru crearea mediului virtual și instalarea dependențelor.

### `Jenkinsfile`

Definește pipeline-ul Jenkins pentru build, verificarea calității codului, testare și deploy în container Docker.

---

## Funcții implementate

În fișierul `app/lib/biblioteca_orase.py` au fost implementate funcțiile:

```python
populatie_reykjavik()
descriere_reykjavik()
```

### `populatie_reykjavik()`

Returnează informații despre populația orașului Reykjavik și despre importanța sa ca principal centru urban, administrativ, economic și cultural al Islandei.

### `descriere_reykjavik()`

Returnează o descriere a orașului Reykjavik, menționând faptul că este capitala Islandei, cunoscută pentru energia geotermală, cultura nordică, arhitectura modernă și apropierea de peisaje naturale spectaculoase.

---

## Rute implementate

Aplicația conține următoarele rute:

```text
/
```

Pagina principală a aplicației.

```text
/orase
```

Pagina temei Orașe.

```text
/orase/reykjavik
```

Pagina dedicată orașului Reykjavik.

```text
/orase/reykjavik/populatie
```

Pagina care afișează informațiile despre populația orașului Reykjavik.

```text
/orase/reykjavik/descriere
```

Pagina care afișează descrierea orașului Reykjavik.

---

## Testare

### Activarea mediului virtual

```bash
. ./activeaza_venv
```

### Rularea testelor

```bash
pytest app/tests/ -v
```

Rezultat obținut:

```text
7 passed
```

Testele verifică:

- funcția `populatie_reykjavik()`;
- funcția `descriere_reykjavik()`;
- ruta `/`;
- ruta `/orase`;
- ruta `/orase/reykjavik`;
- ruta `/orase/reykjavik/populatie`;
- ruta `/orase/reykjavik/descriere`.

### Rularea locală a aplicației

```bash
python3 orase.py
```

Rute verificate local în browser:

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/orase
http://127.0.0.1:5000/orase/reykjavik
http://127.0.0.1:5000/orase/reykjavik/populatie
http://127.0.0.1:5000/orase/reykjavik/descriere
```

---

## Jenkins

Proiectul conține un fișier `Jenkinsfile`.

Pipeline-ul Jenkins are următoarele etape:

1. **Build**
   - creează mediul virtual Python;
   - instalează dependențele din `quickrequirements.txt`.

2. **Calitate Cod**
   - rulează `pylint` pe fișierele din aplicație și teste;
   - este folosit `--exit-zero`, astfel încât pipeline-ul să continue și să afișeze rezultatele.

3. **Testare**
   - rulează testele automate cu `pytest`.

4. **Deploy**
   - construiește imaginea Docker;
   - oprește containerul vechi, dacă există;
   - șterge containerul vechi, dacă există;
   - pornește containerul nou pe portul `5011`.

Rezultate obținute:

- pipeline Jenkins finalizat cu succes;
- testele automate au trecut;
- aplicația a fost pregătită pentru rulare în container.

### Capturi Jenkins

#### Build reușit în Jenkins

![jenkins build success](docs/imagini/jenkins_build_success.png)

#### Console Output Jenkins

![jenkins console output](docs/imagini/jenkins_console_output.png)

---

## Docker

Containerizarea aplicației a fost realizată folosind `Dockerfile`.

Imaginea Docker este construită cu:

```bash
docker build -t orase_reykjavik:latest .
```

Containerul este pornit cu:

```bash
docker stop orase_container || true
docker rm orase_container || true
docker run -d --name orase_container -p 5011:5011 orase_reykjavik:latest
```

Verificarea containerului:

```bash
docker ps
```

Verificarea logurilor:

```bash
docker logs orase_container
```

Aplicația din container a fost accesată în browser la:

```text
http://localhost:5011/
http://localhost:5011/orase
http://localhost:5011/orase/reykjavik
http://localhost:5011/orase/reykjavik/populatie
http://localhost:5011/orase/reykjavik/descriere
```

Logurile containerului au confirmat accesarea rutelor cu status `200`.

---

## Git și GitHub

Am lucrat pe branch-ul personal:

```text
dev_ruxandra_apostol
```

Modificările au fost salvate prin commit și trimise pe GitHub prin push.

A fost realizat Pull Request către branch-ul personal principal:

```text
dev_ruxandra_apostol -> main_ruxandra_apostol
```

Pull Request-ul a fost verificat și integrat.

---

## Pull Request-uri și review

### Pull Request realizat

A fost realizat Pull Request din:

```text
dev_ruxandra_apostol
```

către:

```text
main_ruxandra_apostol
```

Pull Request-ul a fost aprobat și integrat în branch-ul principal personal.

### Review primit

Am primit review de la un coleg din grupă, conform cerințelor proiectului.

### Review oferit

Am participat la procesul de code review în cadrul proiectului de grupă.

---

## Stadiul implementării

### Realizat

- [x] alegerea orașului Reykjavik;
- [x] implementarea aplicației Flask;
- [x] implementarea fișierului `orase.py`;
- [x] implementarea bibliotecii `app/lib/biblioteca_orase.py`;
- [x] implementarea funcțiilor `populatie_reykjavik()` și `descriere_reykjavik()`;
- [x] implementarea rutelor Flask;
- [x] implementarea testelor automate;
- [x] rularea testelor cu `pytest`;
- [x] crearea fișierului `pytest.ini`;
- [x] crearea fișierului `quickrequirements.txt`;
- [x] crearea fișierului `Dockerfile`;
- [x] crearea scriptului `dockerstart.sh`;
- [x] crearea scriptului `activeaza_venv`;
- [x] crearea scriptului `activeaza_venv_jenkins`;
- [x] crearea fișierului `Jenkinsfile`;
- [x] rularea pipeline-ului Jenkins;
- [x] build Jenkins cu succes;
- [x] teste trecute în Jenkins;
- [x] build imagine Docker;
- [x] pornire container Docker;
- [x] accesare aplicație din container;
- [x] verificare loguri Docker;
- [x] capturi de ecran pentru Jenkins;
- [x] capturi de ecran pentru Docker;
- [x] commit și push pe GitHub;
- [x] Pull Request către `main_ruxandra_apostol`;
- [x] review primit de la coleg.

---

## Ce mai este de făcut

- verificarea finală înainte de prezentare;
- rularea aplicației în container;
- demonstrarea testelor, Jenkins și Docker în cadrul susținerii;
- integrarea documentației la nivelul branch-ului `main`, dacă este necesar conform cerințelor de grupă.

---

## Capturi de ecran

### Imaginea Docker creată

![docker images](docs/imagini/docker_images.png)

### Containerul creat pe baza imaginii

![docker ps](docs/imagini/docker_ps_a.png)

### Browserul care accesează aplicația rulată în container

![browser aplicatie](docs/imagini/browser_reykjavik.png)

### Mesajele afișate în consola containerului

![docker logs](docs/imagini/docker_logs.png)

### Jenkins build success

![jenkins build success](docs/imagini/jenkins_build_success.png)

### Jenkins console output

![jenkins console output](docs/imagini/jenkins_console_output.png)

---

## Concluzie

Proiectul implementează funcționalitatea pentru orașul **Reykjavik** în cadrul temei **Orașe**.

Aplicația este funcțională, testele trec, pipeline-ul Jenkins a fost configurat, iar aplicația a fost containerizată cu Docker și accesată din browser.

Proiectul este pregătit pentru prezentare.
