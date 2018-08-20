import argparse
import logging.config
import tspm.control

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)


def setup_parser():
    logger.debug('attempting to setup the parser')
    p = argparse.ArgumentParser(description='tspm calibration tool')

    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--reset',
        action='store_true',
        default=False,
        required=False,
        help='reset system only'
    )
    group.add_argument(
        '--reset-all',
        action='store_true',
        default=False,
        required=False,
        help='reset system & network connections'
    )
    group.add_argument(
        '--read',
        action='store',
        nargs=1,
        type=int,
        required=False,
        help='read any register 0-40'
    )
    group.add_argument(
        '--write',
        action='store',
        nargs=2,
        type=int,
        required=False,
        help='write any value into any of the 0-40 registers'
    )
    group.add_argument(
        '--spi-read',
        action='store',
        nargs=1,
        type=int,
        required=False,
        help='read SPI FIFO register 3-4, returns 408 values'
    )
    group.add_argument(     # TODO: test this what are the 408 values?
        '--spi-write',
        action='store',
        nargs=2,
        type=int,
        required=False,
        help='write 408 values into FIFO register 3-4'
    )
    group.add_argument(     # TODO: most likely not required as this is standalone only!
        '--cleanup',
        action='store_true',
        default=False,
        required=False,
        help='clean up haning udp objects'

    )

    p.add_argument('--version', action='version', version=tspm.VERSION)
    return p


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info('starting ring calibration')
    parser = setup_parser()
    args = parser.parse_args()

    if args.cleanup:
        logger.info('attempting cleanup of calibration')
        tspm.control.clean_up_command()
    elif args.read is not None:
        logger.info('attempting to read from register %d' % args.read[0])
        tspm.control.register_read_command(register=args.read[0])
    elif args.reset:
        logger.info('attempting reset of system')
        tspm.control.reset_command()
    elif args.reset_all:
        logger.info('attempting reset of system and network')
        tspm.control.reset_all_command()
    elif args.spi_read is not None:
        logger.info('attempting to read from SPI register %d' % args.spi_read[0])
        tspm.control.spi_read_command(register=args.spi_read[0])
    elif args.spi_write is not None:
        logger.info('attempting to write %d to SPI register %d' % (args.spi_write[1], args.spi_write[0]))
        tspm.control.spi_write_command(register=args.spi_write[0], value=args.spi_write[0])
    elif args.write is not None:
        logger.info('attempting to write %d to register %d' % (args.write[1], args.write[0]))
        tspm.control.register_write_command(register=args.write[0], value=args.write[1])
