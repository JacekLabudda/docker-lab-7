# Docker – bezpieczeństwo, anty-wzorce i typowe błędy

Repozytorium demonstracyjne do zajęć:

**Docker i konteneryzacja - od podstaw do środowisk produkcyjnych**

Projekt przedstawia bardzo prostą aplikację w Pythonie, uruchamianą w kontenerze Docker, która komunikuje się z zewnętrznym, publicznym API.  

Celem ćwiczenia jest **analiza konfiguracji Dockera i aspektów bezpieczeństwa**, a nie logika biznesowa.

---

## Cel projektu
Celem projektu jest zapoznanie się z:
- rzeczywistymi problemami bezpieczeństwa w projektach Dockerowych
- sposobem przekazywania wrażliwych danych do aplikacji
- konsekwencjami złych decyzji konfiguracyjnych
- analizą obrazu, kontenera i jego relacji z hostem

Projekt **nie jest przykładem dobrych praktyk**.  
Wręcz przeciwnie, ponieważ zawiera wiele rozwiązań, które w środowisku produkcyjnym byłyby nieakceptowalne.

Aplikacja:
- działa jako prosty backend HTTP (Flask)
- przy starcie pobiera dane z zewnętrznego API pogodowego
- zwraca dane w formacie JSON
- do komunikacji z API używa klucza dostępowego

## Struktura repozytorium
```text
.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```
- `app.py` - aplikacja Python/Flask
- `.env.example` - przykładowy plik zmiennych środowiskowych
- `docker-compose.yml` - konfiguracja środowisk Compose

## Przygotowanie projektu (ważne)
Projekt korzysta z pliku `.env` do konfiguracji zmiennych środowiskowych.

1️⃣ Skopiuj plik `.env`

Przed pierwszym uruchomieniem koniecznie wykonaj:
```shell
  cp .env.example .env
```

Następnie możesz (opcjonalnie) dostosować wartość w pliku `.env`.

## Jak uruchomić
### 2️⃣ Uruchom środowisko
```shell
  docker compose up --build
```
Po uruchomieniu aplikacja będzie dostępna pod adresem: http://localhost:5555
### 3️⃣ Zatrzymanie środowiska
```shell
  docker compose down
```

## Uwagi
- Projekt jest celowo uproszczony
- Kod aplikacji nie jest celem ćwiczenia
- Niektóre decyzje konfiguracyjne są **świadomie kontrowersyjne**
- Repozytorium symuluje sytuacje spotykane w prawdziwych projektach