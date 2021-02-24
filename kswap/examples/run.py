def test_initialise():
  from swap import SWAP
  from config import Config
  swap = SWAP(config=Config())
  swap = swap.load()
  swap.get_golds('./data/supernova-hunters-gold-labels.csv')
  swap.apply_golds('./data/supernova-hunters-example-classifications.csv')
  swap.process_classifications_from_csv_dump('./data/supernova-hunters-example-classifications.csv')
  swap.save()
  del swap
  swap = SWAP(config=Config())
  swap = swap.load()

def test_kswap_initialise():
  from kswap import kSWAP
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

def test_offline():
  from swap import SWAP
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
  from kswap import kSWAP
  from kswap_offline_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_offline('./data/kswap-demo-gold-labels.csv',
                   './data/kswap-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_online():
  from swap import SWAP
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
  from kswap import kSWAP
  from kswap_online_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_online('./data/kswap-demo-gold-labels.csv',
                   './data/kswap-demo-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def test_kswap_dmc_use_case():
  from dmc_example.kswap_dmc_use_case import kSWAP
  from dmc_example.dmc_use_case_config import Config
  swap = kSWAP(config=Config())
  swap = swap.load()
  swap.run_online('./dmc_example/data/minion-zoo-dmc-example-gold-labels.csv',
                   './dmc_example/data/minion-zoo-dmc-example-classifications.csv')
  swap.save()
  del swap
  swap = kSWAP(config=Config())
  swap = swap.load()

def compare_offline_and_online_user_scores(user_id):
  from swap import SWAP
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
  from kswap import kSWAP
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

def plot_dmc_use_case_example(user_id):
  import matplotlib.pyplot as plt
  from dmc_example.kswap_dmc_use_case import kSWAP
  from dmc_example.dmc_use_case_config import Config
  from dmc_example.dmc_minion_zoo_config import Config as minion_zoo_config
  swap = kSWAP(config=Config())
  swap = swap.load()
  user = swap.users[user_id]

  try:
    latent_cm = minion_zoo_config().minions[user_id].confusion_matrix
  except AttributeError as e:
    print(repr(e))
    print(e)
    print(e.args)
    exit()

  plt.plot(range(100),
           [latent_cm[0]]*100,
           'k--',
           label='latent performance')

  plt.plot(range(len(user.history)),
           [h[1]['1'][0] for h in user.history],
           color='#EF476F')

  plt.plot(range(len(user.history)),
           [h[1]['2'][1] for h in user.history],
           color='#26C485')
           
  plt.plot(range(len(user.history)),
           [h[1]['N'][2] for h in user.history],
           color='#26547C')

  plt.xlim(0,100)
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

  #compare_kswap_offline_and_online_user_scores(user_id=1)

  ### DMC use case test
  #test_kswap_dmc_use_case()
  plot_dmc_use_case_example(user_id=8)

if __name__ == '__main__':
  main()
