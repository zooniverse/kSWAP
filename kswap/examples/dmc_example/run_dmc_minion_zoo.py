from dmc_minion_zoo_config import Config
from minion_zoo.generate_classifications import generate_classifications

def run_example():

  generate_classifications(Config())

def main():
  run_example()

if __name__ == '__main__':
  main()
