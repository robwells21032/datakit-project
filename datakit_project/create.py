import logging
import os

from cliff.command import Command


class Create(Command):
    "Create a new project"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Create, self).get_parser(prog_name)
        parser.add_argument('name', help="Name of project to create")
        return parser

    def take_action(self, parsed_args):
        self.log.info("CREATE PROJECT: {}".format(parsed_args.name))
        return parsed_args.name