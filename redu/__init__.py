from pkg_resources import get_distribution, DistributionNotFound
from redu.utils import *

try:
    __version__ = get_distribution('redu').version
except DistributionNotFound:
    __version__ = '(local)'
