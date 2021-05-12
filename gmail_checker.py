# -*- coding: utf-8 -*-
import logging
import os

from simplegmail import Gmail

from email.header import decode_header
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class Gmail_checker(NeuronModule):
    def __init__(self, **kwargs):
        super(Gmail_checker, self).__init__(**kwargs)

        self.client_secret_file = kwargs.get('client_secret_file', None)

        # check if parameters have been provided
        if self._is_parameters_ok():
            # prepare a returned dict
            returned_dict = dict()

            gmail = Gmail(client_secret_file=self.client_secret_file)

            # Unread messages in your inbox
            unread = gmail.get_unread_inbox()

            returned_dict["unread"] = len(unread)

            if len(unread) > 0:
                # add a list of subject
                subject_list = list()
                for email in unread:
                    subject = email.subject
                    subject_list.append(subject)

                returned_dict["subjects"] = subject_list

            logger.debug("gmail neuron returned dict: %s" % str(returned_dict))

            self.say(returned_dict)

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: MissingParameterException
        """
        if self.client_secret_file is None:
            raise MissingParameterException("client_secret_file parameter required")

        return True