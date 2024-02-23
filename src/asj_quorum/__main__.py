import logging

from asj_quorum import process

_log = logging.set_logger(__name__)

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  _log.debug("hello world")