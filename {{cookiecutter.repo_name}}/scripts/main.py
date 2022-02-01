"""
Module Docstring.

author:{{cookiecutter.author}}
date:{{cookiecutter.date}}
"""
import argparse
import logging
import cv2
import numpy as np


# Initialize logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO) # Add filename='example.log' for logging to file


def argument_parser():
    """
    Parse arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--opt_str", type=str,
                        default="string_arg",
                        help="Optional string argument")
    parser.add_argument("--opt_bool", type=bool,
                        default=True,
                        help="Optional bool argument")
    parser.add_argument("--opt_int", type=int,
                        default=0,
                        help="Optional int argument")
    return parser.parse_args()


def main(args):
    """
    Implement the main function.
    """
    log.info("Optional arguments: {}, {}, {}".format(args.opt_str, args.opt_bool,
        args.opt_int))
    log.info("Hello, {{cookiecutter.author}}!")


if __name__=="__main__":
    args = argument_parser()
    main(args)
