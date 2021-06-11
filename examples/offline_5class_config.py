class Config(object):
  def __init__(self):
    # panoptes
    self.project = 0
    self.workflow = 0

    # data paths
    self.swap_path = './'
    self.data_path = './data/'
    self.db_name = 'kswap_5class_offline.db'
    self.db_path = './'

    self.user_default = {'0':[0.04, 0.04, 0.04, 0.04, 0.04], '1':[0.04, 0.04, 0.04, 0.04, 0.04], '2':[0.04, 0.04, 0.04, 0.04, 0.04], '3':[0.04, 0.04, 0.04, 0.04, 0.04], '5':[0.04, 0.04, 0.04, 0.04, 0.04]}
    self.label_map = {'0':0, '1':1, '2':2, '3':3, '5':4}
    self.classes = ['0', '1', '2', '3', '5']
    self.p0 = {'0': 0.2, '1': 0.2, '2': 0.2, '3':0.2, '5':0.2}
    self.gamma = 1
    self.thresholds = (0.9, 0.9, 0.9, 0.9, 0.9)
    self.retirement_limit = 10
