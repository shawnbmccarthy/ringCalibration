# need to clean this up (once we understand how these functions work)
# TODO: in progress need to test packet formats

# some simple version information
VERSION = '0.0.1-ALPHA'

# default UDP device information
DEFAULT_UDP_IP = '192.168.120.1'
UDP_WRITE_PORT = 32000

# default cmd ports for device
UDP_CMD_WRITE_PORT = 32001
UDP_CMD_READ_PORT = 32002

# the command data packet contents
DATA_PACKET = [
    0xDE, # header for packet
    0xAD,
    0xBE,
    0xEF,
    0x00, # register address field
    0x00, # register
    0x00, # value
    0x00, # value
    0x00, # value
    0x00, # value
    0xFF, # last 2 bytes always 0xff
    0xFF
]

# used to pack the write packet and unpack the read packet using struct
DATA_PACKET_WFMT = 'HHHHHHHHHHHH'
DATA_PACKET_RFMT = 'HHHHHHHHHHHHHHHHHH'

# tspm commands that we find
TSPM_COMMANDS = {
    'RESET': 0x3E,
    'RESET_ALL': 0x3F
}