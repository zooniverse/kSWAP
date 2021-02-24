import csv

with open('./data/supernova-hunters-example-classifications.csv', 'r') as f, \
     open('./data/tmp.csv', 'w') as o:

  anon_ids = {}
  counter = 0
  reader = csv.DictReader(f)
  for row in reader:
    del row['user_name']
    fieldnames = list(row.keys())
    break
  writer = csv.DictWriter(o, fieldnames=fieldnames)
  for row in reader:
    if 'not-logged-in' in row['user_name']:
      continue
    del row['user_name']
    try:
      anon_id = anon_ids[row['user_id']]
    except KeyError:
      counter += 1
      anon_ids[row['user_id']] = counter
      anon_id = anon_ids[row['user_id']]
    row['user_id'] = anon_id
    writer.writerow(row)
