#!/usr/bin/env python
#
# trello_if.py - Interface to Trello
#
# Copyright (C) 2020 Michael Davies <michael@the-davies.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# Or try here: http://www.fsf.org/copyleft/gpl.html

import sys
import os

from trello import TrelloClient

from trellotool import config


member_store = {}
client = None


def check_credentials():

    global client

    # get_credentials() will exit() if it can't be satisfied
    api_key, api_secret = config.get_credentials()

    client = TrelloClient(
        api_key=api_key,
        api_secret=api_secret
    )


def get_boards():
    boards = client.list_boards()
    return boards


def get_board(board_id):
    return client.get_board(board_id)


def get_list(list_id):
    return client.get_list(list_id)


def get_lists(board_obj):
    return board_obj.all_lists()


def get_cards(list_id):
    # TODO(mrda): We should be using the paging interface here
    tlist = client.get_list(list_id)
    return tlist.list_cards()


def get_member_info(member_id):
    try:
        return member_store[member_id]
    except KeyError:
        member_obj = client.get_member(member_id)
        member_store[member_id] = member_obj
        return member_obj


def add_card(tlist_name, card_title, card_description):
    tlist_id = config.get_list_id_by_name(tlist_name)

    if tlist_id is None:
        print("Error: Couldn't not find list, so can't add card")
        sys.exit(2)

    tlist = client.get_list(tlist_id)
    tlist.add_card(name=card_title,
                   desc=card_description)


def get_card(card_id):
    return client.get_card(card_id)
