from pkg_resources import get_distribution, DistributionNotFound
from bop_refubium.utils import *
#from redu.search import *


HOSTS=["https://refubium.fu-berlin.de/"]

try:
    __version__ = get_distribution('bop_refubium').version
except DistributionNotFound:
    __version__ = '(local)'
