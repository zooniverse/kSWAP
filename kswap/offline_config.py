class Config(object):
  def __init__(self):
    # panoptes
    self.project = 2455
    self.workflow = 1737

    # data paths
    self.swap_path = './'
    self.data_path = self.swap_path+'/data/'
    self.db_name = 'offline_swap.db'
    self.db_path = './data/'

    self.user_default = {'No':0.5, 'Yes':0.5}
    self.label_map = {'No':0, 'Yes':1}
    self.classes = ['No', 'Yes']
    self.p0 = 0.12
    self.gamma = 1
    self.thresholds = (0.01, 0.9)
    self.retirement_limit = 10
