from pkg_resources import get_distribution, DistributionNotFound
from bop.utils import *
#from redu.search import *


HOSTS=["https://depositonce.tu-berlin.de/"]

try:
    __version__ = get_distribution('bop').version
except DistributionNotFound:
    __version__ = '(local)'
