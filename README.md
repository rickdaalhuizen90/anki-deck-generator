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

## Todo
Issue: 400 POST: Too many text segments.
Fix: translate words in batches of 100.

_Resources_
- https://github.com/kerrickstaley/genanki
- https://stackabuse.com/text-translation-with-google-translate-api-in-python/
