from download import download
from .io import url_db, path_target 

def dl_db(url=url_db, target_name=path_target):
  download(url, target_name, replace=False)
