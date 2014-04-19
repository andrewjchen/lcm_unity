"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

import header

class piemos_field_cmd(object):
    __slots__ = ["header", "isFlash", "isStart", "isLeft", "rfid_uid"]

    def __init__(self):
        self.header = None
        self.isFlash = False
        self.isStart = False
        self.isLeft = False
        self.rfid_uid = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(piemos_field_cmd._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == header.header._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack(">bbbq", self.isFlash, self.isStart, self.isLeft, self.rfid_uid))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != piemos_field_cmd._get_packed_fingerprint():
            raise ValueError("Decode error")
        return piemos_field_cmd._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = piemos_field_cmd()
        self.header = header.header._decode_one(buf)
        self.isFlash, self.isStart, self.isLeft, self.rfid_uid = struct.unpack(">bbbq", buf.read(11))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if piemos_field_cmd in parents: return 0
        newparents = parents + [piemos_field_cmd]
        tmphash = (0x41930ef51bb056ba+ header.header._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if piemos_field_cmd._packed_fingerprint is None:
            piemos_field_cmd._packed_fingerprint = struct.pack(">Q", piemos_field_cmd._get_hash_recursive([]))
        return piemos_field_cmd._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
