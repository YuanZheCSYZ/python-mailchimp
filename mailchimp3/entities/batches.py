# coding=utf-8
"""
The Batch Operations API Endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/batches/
Schema: https://api.mailchimp.com/schema/3.0/Batches/Instance.json
"""
from __future__ import unicode_literals

import six
import sys

from mailchimp3.baseapi import BaseApi


class Batches(BaseApi):
    """
    Use batch operations to complete multiple operations with a single call.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Batches, self).__init__(*args, **kwargs)
        self.endpoint = 'batches'
        self.batch_id = None
        self.operation_status = None


    def create(self, data):
        """
        Begin processing a batch operations request.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "operations": array*
            [
                {
                    "method": string* (Must be one of "GET", "POST", "PUT", or "PATCH")
                    "path": string*,
                }
            ]
        }
        """
        try:
            test = data['operations']
        except KeyError as error:
            new_msg = 'The batch must have operations, {}'.format(error)
            six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        for op in data['operations']:
            try:
                test = op['method']
            except KeyError as error:
                new_msg = 'The batch operation must have a method, {}'.format(error)
                six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
            if op['method'] not in ['GET', 'POST', 'PUT', 'PATCH']:
                raise ValueError('The batch operation method must be one of "GET", "POST", "PUT", or "PATCH", not {0}'
                                 ''.format(op['method']))
            try:
                test = op['path']
            except KeyError as error:
                new_msg = 'The batch operation must have a path, {}'.format(error)
                six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        return self._mc_client._post(url=self._build_path(), data=data)


    def all(self, get_all=False, **queryparams):
        """
        Get a summary of batch requests that have been made.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.batch_id = None
        self.operation_status = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, batch_id, **queryparams):
        """
        Get the status of a batch request.

        :param batch_id: The unique id for the batch operation.
        :type batch_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.batch_id = batch_id
        self.operation_status = None
        return self._mc_client._get(url=self._build_path(batch_id), **queryparams)


    def delete(self, batch_id):
        """
        Stops a batch request from running. Since only one batch request is
        run at a time, this can be used to cancel a long running request. The
        results of any completed operations will not be available after this
        call.

        :param batch_id: The unique id for the batch operation.
        :type batch_id: :py:class:`str`
        """
        self.batch_id = batch_id
        self.operation_status = None
        return self._mc_client._delete(url=self._build_path(batch_id))
