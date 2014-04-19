"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

import header

class piemos_cmd(object):
    __slots__ = ["header", "auton", "enabled", "is_blue", "game_time"]

    def __init__(self):
        self.header = None
        self.auton = False
        self.enabled = False
        self.is_blue = False
        self.game_time = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(piemos_cmd._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == header.header._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack(">bbbi", self.auton, self.enabled, self.is_blue, self.game_time))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != piemos_cmd._get_packed_fingerprint():
            raise ValueError("Decode error")
        return piemos_cmd._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = piemos_cmd()
        self.header = header.header._decode_one(buf)
        self.auton, self.enabled, self.is_blue, self.game_time = struct.unpack(">bbbi", buf.read(7))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if piemos_cmd in parents: return 0
        newparents = parents + [piemos_cmd]
        tmphash = (0xa6ee79d563b22a14+ header.header._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if piemos_cmd._packed_fingerprint is None:
            piemos_cmd._packed_fingerprint = struct.pack(">Q", piemos_cmd._get_hash_recursive([]))
        return piemos_cmd._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
