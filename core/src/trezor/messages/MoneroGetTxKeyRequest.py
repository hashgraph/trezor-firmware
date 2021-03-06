# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroGetTxKeyRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 550

    def __init__(
        self,
        address_n: List[int] = None,
        network_type: int = None,
        salt1: bytes = None,
        salt2: bytes = None,
        tx_enc_keys: bytes = None,
        tx_prefix_hash: bytes = None,
        reason: int = None,
        view_public_key: bytes = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.network_type = network_type
        self.salt1 = salt1
        self.salt2 = salt2
        self.tx_enc_keys = tx_enc_keys
        self.tx_prefix_hash = tx_prefix_hash
        self.reason = reason
        self.view_public_key = view_public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('network_type', p.UVarintType, 0),
            3: ('salt1', p.BytesType, 0),
            4: ('salt2', p.BytesType, 0),
            5: ('tx_enc_keys', p.BytesType, 0),
            6: ('tx_prefix_hash', p.BytesType, 0),
            7: ('reason', p.UVarintType, 0),
            8: ('view_public_key', p.BytesType, 0),
        }
