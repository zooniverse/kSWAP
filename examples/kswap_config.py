class Config(object):
  def __init__(self):
    # panoptes
    self.project = 0
    self.workflow = 0

    # data paths
    self.swap_path = './'
    #self.data_path = self.swap_path+'/data/'
    self.data_path = self.swap_path
    self.db_name = 'kswap.db'
    #self.db_path = './data/'
    self.db_path = self.swap_path

    self.user_default = {'0':[0.33, 0.33, 0.33], '1':[0.33, 0.33, 0.33], '2':[0.33, 0.33, 0.33]}
    self.label_map = {'0':0, '1':1, '2':2}
    #self.classes = ['0', '1', '2']
    self.p0 = {'0': 0.1, '1': 0.1, '2': 0.1}
    self.gamma = 1
    self.thresholds = (0.9, 0.9, 0.9)
    self.retirement_limit = 10
