class Config(object):
  def __init__(self):
    # panoptes
    self.project = 0
    self.workflow = 0

    # data paths
    self.swap_path = './'
    self.data_path = self.swap_path+'dmc_example/data/'
    self.db_name = 'kswap_dmc_example.db'
    self.db_path = './dmc_example/data/'

    self.user_default = {'1':[0.5, 0.0, 0.5], '2':[0.0, 0.5, 0.5], 'N':[0.33, 0.33, 0.33]}
    #self.label_map = {'0':0, '1':1, '2':2}
    self.label_map = {'1':[0, 2, 2], '2':[2,1,2], 'N':[0,1,2]}
    self.classes = ['1', '2', 'N']
    self.p0 = {'1': 0.1, '2': 0.1, 'N': 0.1}
    self.gamma = 1
    self.thresholds = (0.01, 0.9)
    self.retirement_limit = 10
