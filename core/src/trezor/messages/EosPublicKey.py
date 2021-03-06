# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class EosPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 601

    def __init__(
        self,
        wif_public_key: str = None,
        raw_public_key: bytes = None,
    ) -> None:
        self.wif_public_key = wif_public_key
        self.raw_public_key = raw_public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('wif_public_key', p.UnicodeType, 0),
            2: ('raw_public_key', p.BytesType, 0),
        }
