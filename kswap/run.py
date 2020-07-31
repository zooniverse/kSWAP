from swap import SWAP

from config import Config
from offline_config import Config as OfflineConfig
from online_config import Config as OnlineConfig

def test_initialise():
  swap = SWAP(config=Config())
  swap.save()
  swap = swap.load()
  swap.get_golds('./data/supernova-hunters-gold-labels.csv')
  swap.apply_golds('./data/supernova-hunters-classifications.csv')
  swap.process_classifications_from_csv_dump('./data/supernova-hunters-example-classifications.csv')
  swap.save()
  del swap
  swap = SWAP(config=Config())
  swap = swap.load()

def test_offline():
  swap = SWAP(config=OfflineConfig())
  swap.save()
  swap = swap.load()
  swap.run_offline('./data/supernova-hunters-gold-labels.csv',
                   './data/supernova-hunters-example-classifications.csv')
  swap.save()
  del swap
  swap = SWAP(config=OfflineConfig())
  swap.save()
  swap = swap.load()

def test_online():
  swap = SWAP(config=OnlineConfig())
  swap.save()
  swap = swap.load()
  swap.run_online('./data/supernova-hunters-gold-labels.csv',
                  './data/supernova-hunters-example-classifications.csv')
  swap.save()
  del swap
  swap = SWAP(config=OnlineConfig())
  swap.save()
  swap = swap.load()

def compare_offline_and_online_user_scores(user_id):
  import matplotlib.pyplot as plt
  
  offline_swap = SWAP(config=OfflineConfig())
  offline_swap = offline_swap.load()
  offline_user = offline_swap.users[user_id]
  
  online_swap = SWAP(config=OnlineConfig())
  online_swap = online_swap.load()
  online_user = online_swap.users[user_id]

  print(len(offline_user.history), len(online_user.history))
  print(offline_user.confusion_matrix, online_user.confusion_matrix)
  print(offline_user.user_score, online_user.user_score)
  assert len(offline_user.history) == len(online_user.history)

  plt.plot(range(len(offline_user.history)),
           [h[1]['Yes'] for h in offline_user.history],
           color='#26547C',
           label='\'Yes\' offline')
  plt.plot(range(len(offline_user.history)),
           [h[1]['No'] for h in offline_user.history],
           color='#EF476F',
           label='\'No\' offline')
  plt.plot(range(len(online_user.history)),
           [h[1]['Yes'] for h in online_user.history],
           color='#26547C',
           ls='--',
           label='\'Yes\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['No'] for h in online_user.history],
           color='#EF476F',
           ls='--',
           label='\'No\' online')
  plt.xlim(0,len(offline_user.history))
  plt.ylim(0,1)
  plt.xlabel('number of classifications')
  plt.ylabel('user score')
  plt.legend(loc='best')
  plt.show()

def main():
  #test_initialise()
  test_offline()
  test_online()

  compare_offline_and_online_user_scores(user_id=1)

if __name__ == '__main__':
  main()
