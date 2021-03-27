# Anki Deck Generator

Translate most common words in an Anki Deck format.

## Docker

build
```
docker build -t anki .
```

run
```
docker run -it anki anki.py
```

or with docker-compose

build
```
docker-compose up --build
```

run
```
docker-compose up
```

## Common problems
- https://stackoverflow.com/questions/65511216/googletrans-stopped-working-with-detecting-all-languages-as-english

_Resources_
- https://github.com/kerrickstaley/genanki
- https://pypi.org/project/googletrans/
- https://stackabuse.com/text-translation-with-google-translate-api-in-python/
