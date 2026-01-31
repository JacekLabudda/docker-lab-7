# Docker – CI/CD, GitHub Actions i publikacja obrazu Docker

Repozytorium demonstracyjne do zajęć:

**Docker i konteneryzacja - od podstaw do środowisk produkcyjnych**

Projekt przedstawia prostą aplikację w Pythonie, która losuje tekst z listy i wypisuje go w konsoli. Aplikacja jest konteneryzowana w Dockerze i publikowana do **Docker Hub** przy użyciu **GitHub Actions**.

Celem ćwiczenia jest **zapoznanie się z procesem CI/CD w praktyce**, publikacją obrazu Docker oraz uruchamianiem go na różnych maszynach.

---

## Cel projektu
Celem projektu jest zapoznanie się z:
- tworzeniem i konteneryzacją prostej aplikacji Python w Dockerze,
- konfiguracją **GitHub Actions** dla testów i publikacji obrazu,
- korzystaniem z **Docker Hub** jako registry obrazów,
- uruchamianiem obrazu Dockera lokalnie lub na innych komputerach.

## Struktura repozytorium
```text
.
├── app.py
├── test_app.py
├── Dockerfile
├── .github/
│   └── workflows/
│       └── publish.yml
└── README.md
```
- `app.py` - aplikacja Python losująca tekst
- `test_app.py` - prosty test pytest sprawdzający, że aplikacja generuje tekst
- `Dockerfile` - budowanie obrazów: testowy i produkcyjny
- `.github/workflows/publish.yml` - workflow **GitHub Actions** publikujący obraz

## Przygotowanie projektu (ważne)
1️⃣ Załóż konto na GitHubie (jeśli jeszcze go nie masz): https://github.com

2️⃣ W prawym górnym rogu obecnego repozytorium kliknij przycisk **Fork**

3️⃣ Wybierz swoje konto jako miejsce utworzenia fork’a

4️⃣ Po chwili GitHub utworzy kopię repozytorium w Twoim koncie:  
`https://github.com/<TwojLogin>/docker-lab-7`

5️⃣ Teraz możesz sklonować repozytorium na komputer:
```bash
  git clone https://github.com/<TwojLogin>/docker-lab-7.git
  cd docker-lab-7
```

6️⃣ Załóż konto na [Docker Hub](https://hub.docker.com/) jeśli jeszcze go nie masz.

7️⃣ Wprowadź sekrety do **GitHub** w repozytorium:
- `DOCKERHUB_USERNAME` - Twój login do **Docker Hub**
- `DOCKERHUB_TOKEN` - Twoje hasło do **Docker Hub**

## Modyfikacja i push zmian
1️⃣ Zmodyfikuj pliki w repo, np. `app.py` lub `test_app.py`.

2️⃣ Zacommituj zmiany i wypchnij na **GitHub**:
```bash
  git add .
  git commit -m "Zmiany w aplikacji"
  git push origin master
```

3️⃣ Po push'u **GitHub Actions** automatycznie:
- zbuduje testowy obraz Dockera z pytestem, 
- uruchomi testy w kontenerze, 
- jeśli testy przejdą, zbuduje produkcjny obraz, 
- opublikuje go do Docker Hub (`<TwojLogin>/docker-lab-7:latest`).

## Uruchomienie obrazu

Na swoim komputerze lub innym:
```bash
  docker run --rm <TwojLogin>/docker-lab-7:latest
```
Przykładowy output:
```text
Python jest super
```
Każde uruchomienie wypisuje losowy tekst z listy.

## Uwagi
- Projekt jest celowo uproszczony, aby skupić się na **CI/CD** i **Dockerze** 
- Testy w tym projekcie to **smoke test** - sprawdzają tylko, że aplikacja coś generuje 
- Workflow **GitHub Actions** uruchamia testy wewnątrz kontenera, co symuluje praktykę profesjonalnego CI/CD 
- Publikacja do **Docker Hub** umożliwia uruchamianie obrazu na dowolnym komputerze 
- Repozytorium pokazuje typowy proces: **modyfikacja kodu → push → testy → build → publikacja → uruchomienie obrazu**