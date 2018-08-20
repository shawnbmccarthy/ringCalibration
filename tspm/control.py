# TODO need to validate commands and controls
import logging
import socket
import struct
import tspm

from numpy import uint8

logger = logging.getLogger(__name__)


def register_read_command(
        register,
        send_to=tspm.DEFAULT_UDP_IP,
        bind_to='',
        r_port=tspm.UDP_CMD_READ_PORT,
        w_port=tspm.UDP_CMD_WRITE_PORT):
    """
    there are 40 registers to read from, attempt to read data from a given register

    :param register:
    :param send_to:
    :param bind_to:
    :param r_port:
    :param w_port:
    :return:
    """
    logger.debug('running register read command on register: %d' % register)
    processing = True

    write_packet = tspm.DATA_PACKET.copy()
    write_packet[5] = register

    write_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    read_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    write_sock.sendto(struct.pack(tspm.DATA_PACKET_WFMT, write_packet), (send_to, w_port))
    read_sock.bind((bind_to, r_port))

    # 18 bytes
    data = None
    # TODO: do we need this loop or will it just wait for the one read
    # TODO: need to test this out
    while processing:
        data, addr = read_sock.recv(18*8)
        logger.info('recieved data from: %s' % addr)
        data = struct.unpack(tspm.DATA_PACKET_RFMT, data)
        processing = False

    if data is not None:
        logger.info('returned data: %s' % data)
    else:
        logger.warning('did not receive valid data!')

    write_sock.close()
    read_sock.close()
    return data


def reset_command():
    """
    send 0x3E reset command to register 0

    :return:
    """
    logger.debug('running reset command(%d)' % tspm.TSPM_COMMANDS['RESET'])
    register_write_command(register=0, value=tspm.TSPM_COMMANDS['RESET'])


def reset_all_command():
    """
    send 0x3F reset all command to register 0

    :return:
    """
    logger.debug('running reset all command(%d)' % tspm.TSPM_COMMANDS['RESET_ALL'])
    register_write_command(register=0, value=tspm.TSPM_COMMANDS['RESET_ALL'])


def register_write_command(register, value, host=tspm.DEFAULT_UDP_IP):
    """
    write a value into register
    :param register:
    :param value:
    :return:
    """
    logger.debug('running write command with value %d on register %d' % (value, register))



def spi_read_command(register):
    """

    :param register:
    :return:
    """
    logger.debug('running spi read command on register %d' % register)


def spi_write_command(register, value):
    """

    :param register:
    :param value:
    :return:
    """
    logger.debug('running spi write command with value %d on register %d' % (value, register))
