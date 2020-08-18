import csv
import json
import random

from kswap_config import Config

def generate_golds(n, classes):
  with open('./data/kswap-demo-gold-labels.csv', 'w') as gold_file:
    writer = csv.writer(gold_file)
    writer.writerow(['subject_id', 'gold'])
    for i in range(n):
      writer.writerow([i,i%(len(classes))])

def generate_classifications(n, users, workflow_id, subjects, classes, competence):
  with open('./data/kswap-demo-classifications.csv', 'w') as cl_file:
    writer = csv.writer(cl_file)
    writer.writerow(['classification_id', 'user_id', 'user_name',
                     'workflow_id', 'annotations', 'metadata', 'subject_ids'])
    for i in range(n):
      classification_id = i
      user_id = users[i%len(users)]
      user_name = user_id
      subject_ids = subjects[i%len(subjects)]
      annotations = json.dumps([{'value':get_value(subject_ids, classes, competence)}])
      #if i < len(subjects):
      #  seen_before = json.dumps({'seen_before':False})
      #else:
      #  seen_before = json.dumps({'seen_before':True})
      seen_before = json.dumps({'seen_before':False})
      writer.writerow([classification_id, user_id, user_name, workflow_id,
                       annotations, seen_before, subject_ids])

def get_value(subject_id, classes, competence):
  if random.random() < competence:
    return str(subject_id%len(classes))
  c = classes[:]
  c.remove(str(subject_id%len(classes)))
  return random.choice(c)

def main():
  
  n_users = 5
  n_subjects = 100
  n_classifications = 1000
  workflow_id = 0
  competence = 0.5
  
  users = [u for u in range(n_users)]
  subjects = [s for s in range(n_subjects)]
  
  config = Config()
  
  generate_golds(n_subjects, config.classes)

  generate_classifications(n_classifications, users, workflow_id, subjects, config.classes, competence)

if __name__ == '__main__':
  main()