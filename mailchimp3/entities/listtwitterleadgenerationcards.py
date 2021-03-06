# coding=utf-8
"""
The List Twitter Leade Generation Cards API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/twitter-lead-gen-cards/
Schema: https://api.mailchimp.com/schema/3.0/Lists/TwitterLeadGenCards/Instance.json
"""
from __future__ import unicode_literals

import six
import sys

from mailchimp3.baseapi import BaseApi
from mailchimp3.helpers import check_url


class ListTwitterLeadGenerationCards(BaseApi):
    """
    Manage Twitter Lead Generation Cards for a specific MailChimp list.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ListTwitterLeadGenerationCards, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.twitter_card_id = None


    def create(self, list_id, data):
        """
        Create a new Twitter Lead Generation Card for a specific list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "name": string*,
            "title": string*,
            "cta_text": string*,
            "privacy_policy_url": string*,
            "image_url": string*,
            "twitter_account_id": string*
        }
        """
        self.list_id = list_id
        try:
            data['name']
        except KeyError as error:
            new_msg = 'The twitter lead generation card must have a name, {}'.format(error)
            six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        try:
            data['title']
        except KeyError as error:
            new_msg = 'The twitter lead generation card must have a title, {}'.format(error)
            six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        try:
            data['cta_text']
        except KeyError as error:
            new_msg = 'The twitter lead generation card must have a cta_text, {}'.format(error)
            six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        if len(data['cta_text']) > 20:
            raise ValueError('The twitter lead generation card cta_text must be 20 characters or less')
        try:
            data['privacy_policy_url']
        except KeyError as error:
            new_msg = 'The twitter lead generation card must have a privacy_policy_url, {}'.format(error)
            six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        check_url(data['privacy_policy_url'])
        try:
            data['image_url']
        except KeyError as error:
            new_msg = 'The twitter lead generation card must have a image_url, {}'.format(error)
            six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        check_url(data['image_url'])
        try:
            data['twitter_account_id']
        except KeyError as error:
            new_msg = 'The twitter lead generation card must have a twitter_account_id, {}'.format(error)
            six.reraise(KeyError, KeyError(new_msg), sys.exc_info()[2])
        response = self._mc_client._post(url=self._build_path(list_id, 'twitter-lead-gen-cards'), data=data)
        if response is not None:
            self.twitter_card_id = response['id']
        else:
            self.twitter_card_id = None
        return response


    def all(self, list_id):
        """
        Get information about all Twitter Lead Generation Cards for a specific list.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        """
        self.list_id = list_id
        self.twitter_card_id = None
        return self._mc_client._get(url=self._build_path(list_id, 'twitter-lead-gen-cards'))


    def get(self, list_id, twitter_card_id):
        """
        Get information about a specific Twitter Lead Generation Card.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param twitter_card_id: The Twitter Lead Generation Card ID.
        :type twitter_card_id: :py:class:`str`
        """
        self.list_id = list_id
        self.twitter_card_id = twitter_card_id
        return self._mc_client._get(url=self._build_path(list_id, 'twitter-lead-gen-cards', twitter_card_id))
