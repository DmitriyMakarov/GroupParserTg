import os
from sys import platform
from pathlib import Path
import configparser
import shutil
from resources import surroundings

config_dir = Path(Path.home(), surroundings.configpath)
config_path = Path(config_dir, 'config')
base_path = Path(config_dir, 'db')
res_example_path = Path(Path.cwd(), 'resources', 'example_config')

if __name__ == "__main__":
    if config_dir.exists() is False:
        os.mkdir(config_dir)
    if config_path.exists() is False:
        shutil.copy(res_example_path, config_path)
    print(platform)
    print(Path.cwd())
    cfg = configparser.ConfigParser()
    cfg.read(config_path)
    cfg.sections()
    print(cfg['DEFAULT']['test_str'])
