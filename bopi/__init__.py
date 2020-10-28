from pkg_resources import get_distribution, DistributionNotFound
from bopi.utils import *


HOSTS=["https://depositonce.tu-berlin.de/"]

try:
    __version__ = get_distribution('bopi').version
except DistributionNotFound:
    __version__ = '(local)'
