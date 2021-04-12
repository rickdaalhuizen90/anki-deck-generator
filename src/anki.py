from google.cloud import translate_v2 as translate
import csv
import genanki
import random

translate_client = translate.Client()
words = []

# Create Anki Deck
uid = random.randrange(1 << 30, 1 << 31)

deck = genanki.Deck(
  uid,
  'indonesian Common Words')

model = genanki.Model(
  uid,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

# Filter words
with open('id.txt') as f:
  lines = f.readlines()

  for line in lines:
    word = line.split()[0]
    frequency = int(line.split()[1])

    if frequency >= 300 and len(word) >= 3:
      words.append(word)

# Translate words
translations = translate_client.translate(words, target_language='nl')
rows = [['Indonesian', 'Dutch']]

for translation in translations:
  origin = translation['input'].capitalize()
  trans = translation['translatedText'].capitalize()

  rows.append([origin, trans])
  deck.add_note(genanki.Note(model=model, fields=[origin, trans]))
  print(f'{origin} -> {trans}')

# Save anki deck
genanki.Package(deck).write_to_file('id_nl.apkg')

#Save results to csv
with open('id_nl.csv', 'w', newline='\n') as file:
  writer = csv.writer(file)
  writer.writerows(rows)