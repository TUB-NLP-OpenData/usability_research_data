from pkg_resources import get_distribution, DistributionNotFound
from redu.utils import *
#from redu.search import *


HOSTS=["https://depositonce.tu-berlin.de/"]

try:
    __version__ = get_distribution('redu').version
except DistributionNotFound:
    __version__ = '(local)'
