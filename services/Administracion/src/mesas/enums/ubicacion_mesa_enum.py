from enum import Enum


class UbicacionMesaEnum(str, Enum):
    INTERIOR = "interior"
    EXTERIOR = "exterior"
    TERRAZA = "terraza"
    VIP = "vip"
