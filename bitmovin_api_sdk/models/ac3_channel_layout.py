# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Ac3ChannelLayout(Enum):
    NONE = "NONE"
    MONO = "MONO"
    CL_STEREO = "STEREO"
    CL_SURROUND = "SURROUND"
    CL_QUAD = "QUAD"
    CL_2_1 = "2.1"
    CL_2_2 = "2.2"
    CL_3_1 = "3.1"
    CL_4_0 = "4.0"
    CL_4_1 = "4.1"
    CL_5_0 = "5.0"
    CL_5_0_BACK = "5.0_BACK"
    CL_5_1 = "5.1"
    CL_5_1_BACK = "5.1_BACK"
