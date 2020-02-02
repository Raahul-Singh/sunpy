"""
This subpackage contains:

* A robust framework for working with coordinate systems
* Functions to obtain the locations of solar-system bodies
  (`sunpy.coordinates.ephemeris`)
* Functions to calculate Sun-specific coordinate information
  (`sunpy.coordinates.sun`)

The diagram below shows all of Sun-based and Earth-based coordinate systems
available through `sunpy.coordinates`, as well as the transformations between
them.  Each frame is labeled with the name of its class and its alias (useful
for converting other coordinates to them using attribute-style access).

The frames colored in cyan are implemented in `astropy.coordinates`, and there
are other astronomical frames that can be transformed to that are not shown
below (see `astropy.coordinates.builtin_frames`).

"""

from .frames import *
from .offset_frame import *
from .transformations import transform_with_sun_center, _make_sunpy_graph
from .ephemeris import *
from . import sun

from .wcs_utils import *

__doc__ += _make_sunpy_graph()
