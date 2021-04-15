class Config(object):
  def __init__(self):
    # panoptes
    self.project = 0
    self.workflow = 0

    # data paths
    self.swap_path = './'
    self.data_path = './data/'
    self.db_name = self.data_path + 'kswap_daniels_online.db'
    self.db_path = './'

    self.classes = ['0', '1', '2', '3']

    self.label_map = {'0': 0,
                      '1': 1,
                      '2': 2,
                      '3': 3}

    self.user_default = {'0': [0.25, 0.25, 0.25, 0.25],
                         '1': [0.25, 0.25, 0.25, 0.25],
                         '2': [0.25, 0.25, 0.25, 0.25],
                         '3': [0.25, 0.25, 0.25, 0.25]}

    self.p0 = {'0': 0.1,
               '1': 0.1,
               '2': 0.1,
               '3': 0.7}

    self.gamma = 1
    self.thresholds = (0.02, 0.99)
    self.retirement_limit = 100
