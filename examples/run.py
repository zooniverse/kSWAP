import sys
sys.path.insert(0, '../kswap')
from swap import SWAP
from kswap import kSWAP

def test_initialise():
  from config import Config
  swap = SWAP(config=Config())
  swap = swap.load()
  swap.get_golds('./data/supernova-hunters-gold-labels.csv')
  swap.apply_golds('./data/supernova-hunters-classifications.csv')
  swap.process_classifications_from_csv_dump('./data/supernova-hunters-example-classifications.csv')
  swap.save()
  del swap
  swap = SWAP(config=Config())
  swap = swap.load()

def test_kswap_initialise():
  from kswap_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.get_golds('./data/kswap-demo-gold-labels.csv')
  swap.apply_golds('./data/kswap-demo-classifications.csv')
  swap.process_classifications_from_csv_dump('./data/kswap-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_5swap_initialise():
  from kswap_5class_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.get_golds('./data/kswap-5class-demo-gold-labels.csv')
  swap.apply_golds('./data/kswap-5class-demo-classifications.csv')
  swap.process_classifications_from_csv_dump('./data/kswap-5class-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_offline():
  from offline_config import Config
  swap = SWAP(config=Config())
  swap = swap.load()
  swap.run_offline('./data/supernova-hunters-gold-labels.csv',
                   './data/supernova-hunters-example-classifications.csv')
  swap.save()
  del swap
  swap = SWAP(config=Config())
  swap = swap.load()

def test_kswap_offline():
  from kswap_offline_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_offline('./data/kswap-demo-gold-labels.csv',
                   './data/kswap-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_5swap_offline():
  from offline_5class_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_offline('./data/kswap-5class-demo-gold-labels.csv',
                   './data/kswap-5class-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_online():
  from online_config import Config
  swap = SWAP(config=Config())
  swap = swap.load()
  swap.run_online('./data/supernova-hunters-gold-labels.csv',
                  './data/supernova-hunters-example-classifications.csv')
  swap.save()
  del swap
  swap = SWAP(config=Config())
  swap = swap.load()

def test_kswap_online():
  from kswap_online_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_online('./data/kswap-demo-gold-labels.csv',
                   './data/kswap-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_5swap_online():
  from online_5class_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_online('./data/kswap-5class-demo-gold-labels.csv',
                   './data/kswap-5class-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_daniels_online():
  from daniels_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_online('./data/daniels-demo-gold-labels.csv',
                   './data/daniels-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def compare_offline_and_online_user_scores(user_id):
  import matplotlib.pyplot as plt
  
  from offline_config import Config as OfflineConfig
  offline_swap = SWAP(config=OfflineConfig())
  offline_swap = offline_swap.load()
  offline_user = offline_swap.users[user_id]
  
  from online_config import Config as OnlineConfig
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

def compare_kswap_offline_and_online_user_scores(user_id):
  import matplotlib.pyplot as plt
  
  from kswap_offline_config import Config as OfflineConfig
  offline_swap = kSWAP(config=OfflineConfig())
  offline_swap = offline_swap.load()
  offline_user = offline_swap.users[user_id]
  
  from kswap_online_config import Config as OnlineConfig
  online_swap = kSWAP(config=OnlineConfig())
  online_swap = online_swap.load()
  online_user = online_swap.users[user_id]

  print(len(offline_user.history), len(online_user.history))
  print(offline_user.confusion_matrix, online_user.confusion_matrix)
  print(offline_user.user_score, online_user.user_score)
  assert len(offline_user.history) == len(online_user.history)
  
  plt.plot(range(len(offline_user.history)),
           [h[1]['0'][0] for h in offline_user.history],
           color='#26547C',
           label='\'0\' offline')
  plt.plot(range(len(offline_user.history)),
           [h[1]['1'][1] for h in offline_user.history],
           color='#EF476F',
           label='\'1\' offline')
  plt.plot(range(len(offline_user.history)),
           [h[1]['2'][2] for h in offline_user.history],
           color='#26C485',
           label='\'2\' offline')
  plt.plot(range(len(online_user.history)),
           [h[1]['0'][0] for h in online_user.history],
           color='#26547C',
           ls='--',
           label='\'0\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['1'][1] for h in online_user.history],
           color='#EF476F',
           ls='--',
           label='\'1\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['2'][2] for h in online_user.history],
           color='#26C485',
           ls='--',
           label='\'2\' online')
  plt.plot(range(len(online_user.history)),
           [0.5 for h in online_user.history],
           color='k',
           ls='--',
           lw=2,
           label='demo competence')
           
  plt.xlim(0,len(offline_user.history))
  plt.ylim(0,1)
  plt.xlabel('number of classifications')
  plt.ylabel('user score')
  plt.legend(loc='best')
  plt.show()

def compare_offline_and_online_user_scores(user_id):
  import matplotlib.pyplot as plt
  
  from offline_config import Config as OfflineConfig
  offline_swap = SWAP(config=OfflineConfig())
  offline_swap = offline_swap.load()
  offline_user = offline_swap.users[user_id]
  
  from online_config import Config as OnlineConfig
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

def compare_5swap_offline_and_online_user_scores(user_id):
  import matplotlib.pyplot as plt
  
  from offline_5class_config import Config as OfflineConfig
  offline_swap = kSWAP(config=OfflineConfig())
  offline_swap = offline_swap.load()
  offline_user = offline_swap.users[user_id]
  
  from online_5class_config import Config as OnlineConfig
  online_swap = kSWAP(config=OnlineConfig())
  online_swap = online_swap.load()
  online_user = online_swap.users[user_id]

  print(len(offline_user.history), len(online_user.history))
  print(offline_user.confusion_matrix, online_user.confusion_matrix)
  print(offline_user.user_score, online_user.user_score)
  assert len(offline_user.history) == len(online_user.history)
  
  plt.plot(range(len(offline_user.history)),
           [h[1]['0'][0] for h in offline_user.history],
           color='#26547C',
           label='\'0\' offline')
  plt.plot(range(len(offline_user.history)),
           [h[1]['1'][1] for h in offline_user.history],
           color='#EF476F',
           label='\'1\' offline')
  plt.plot(range(len(offline_user.history)),
           [h[1]['2'][2] for h in offline_user.history],
           color='#26C485',
           label='\'2\' offline')
  plt.plot(range(len(offline_user.history)),
           [h[1]['3'][3] for h in offline_user.history],
           color='#FFD400',
           label='\'3\' offline')
  plt.plot(range(len(offline_user.history)),
           [h[1]['5'][4] for h in offline_user.history],
           color='#3ABEFF',
           label='\'5\' offline')
  plt.plot(range(len(online_user.history)),
           [h[1]['0'][0] for h in online_user.history],
           color='#26547C',
           ls='--',
           label='\'0\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['1'][1] for h in online_user.history],
           color='#EF476F',
           ls='--',
           label='\'1\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['2'][2] for h in online_user.history],
           color='#26C485',
           ls='--',
           label='\'2\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['3'][3] for h in online_user.history],
           color='#FFD400',
           ls='--',
           label='\'3\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['5'][4] for h in online_user.history],
           color='#3ABEFF',
           ls='--',
           label='\'5\' online')
  plt.plot(range(len(online_user.history)),
           [0.5 for h in online_user.history],
           color='k',
           ls='--',
           lw=2,
           label='demo competence')
           
  plt.xlim(0,len(offline_user.history))
  plt.ylim(0,1)
  plt.xlabel('number of classifications')
  plt.ylabel('user score')
  plt.legend(loc='best')
  plt.show()

def plot_daniels_online(user_id):
  import matplotlib.pyplot as plt
  
  from daniels_config import Config
  online_swap = kSWAP(config=Config())
  online_swap = online_swap.load()
  online_user = online_swap.users[user_id]

  plt.plot(range(len(online_user.history)),
           [h[1]['0'][0] for h in online_user.history],
           color='#26547C',
           ls='--',
           label='\'0\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['1'][1] for h in online_user.history],
           color='#EF476F',
           ls='--',
           label='\'1\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['2'][2] for h in online_user.history],
           color='#26C485',
           ls='--',
           label='\'2\' online')
  plt.plot(range(len(online_user.history)),
           [h[1]['3'][3] for h in online_user.history],
           color='#FFD400',
           ls='--',
           label='\'3\' online')
  plt.plot(range(len(online_user.history)),
           [0.73 for h in online_user.history],
           color='k',
           ls='--',
           lw=2,
           label='demo competence (0.73)')
           
  plt.xlim(0,len(online_user.history))
  plt.ylim(0,1)
  plt.xlabel('number of classifications')
  plt.ylabel('user score')
  plt.legend(loc='best')
  plt.show()

def main():

  ### SWAP tests
  #test_initialise()
  #test_offline()
  #test_online()

  #compare_offline_and_online_user_scores(user_id=1)

  ### kSWAP tests
  #test_kswap_initialise()
  #test_kswap_offline()
  #test_kswap_online()

  #compare_kswap_offline_and_online_user_scores(user_id=0)

  ### 5SWAP example
  #test_5swap_initialise()
  #test_5swap_offline()
  #test_5swap_online()

  #compare_5swap_offline_and_online_user_scores(user_id=7)

  ### Daniel's example
  test_daniels_online()
  plot_daniels_online(1)

if __name__ == '__main__':
  main()
