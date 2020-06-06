from pkg_resources import get_distribution, DistributionNotFound
from utils import *

try:
    __version__ = get_distribution('redu').version
except DistributionNotFound:
    __version__ = '(local)'
