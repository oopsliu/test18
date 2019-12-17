#!/usr/bin/env python3

from __future__ import print_function

import urllib.request, urllib.error, urllib.parse as parse
import json
import base64
import sys, os
import time
import datetime
import argparse, configparser
import functools


repository = 'https://api.github.com/repos/ArcGIS/survey123-webform'
username = 'l.z.lz@hotmail.com'
token =  ''

def progress_msg(*msgs):
    now = datetime.datetime.now()
    print('[{0}]'.format(now), *msgs)

def error_msg(*msgs):
    now = datetime.datetime.now()
    print('[{0}]'.format(now), *msgs, file=sys.stderr)
    
def send_request(url, post_data=None, method=None, content_length=None,
                 custom_media_type=None,
                 can_retry=True):

    
    if post_data is not None:
        post_data = json.dumps(post_data).encode("utf-8")
    
    full_url = "%s/%s" % (repository, url)
    print(full_url)

    req = urllib.request.Request(full_url, data=post_data, method=method)

    req.add_header("Authorization", b"Basic " + base64.urlsafe_b64encode(username.encode("utf-8") + b":" + token.encode("utf-8")))
    req.add_header("Content-Type", "application/json")
    if content_length is not None:
        req.add_header("Content-Length", content_length)
    req.add_header("Accept", "application/json")
    if custom_media_type is not None:
        req.add_header("Accept", custom_media_type)
    req.add_header("User-Agent", "zadarastorage")

    while True:
        try:
            response = urllib.request.urlopen(req)
            json_data = response.read()
            break
        except urllib.error.HTTPError as error:
            error_details = error.read();
            error_details = json.loads(error_details.decode("utf-8"))
            if 'message' in error_details and\
               error_details['message'].startswith('You have triggered an abuse detection mechanism and have been temporarily blocked from content creation') or\
               error_details['message'].startswith('API rate limit exceeded'):
                progress_msg('    .... GITHUB RATE LIMITING HIT, SLEEP ...')
                time.sleep(60)
                continue
            error_msg('HTTP ERROR: {0} {1}'.format(error.code, error.reason))
            error_msg('Request: {0}, data: {1}'.format(url, post_data))
            error_msg('ERROR DETAILS:')
            for detail in error_details:
                error_msg('==={0}===:'.format(detail))
                error_msg(error_details[detail])
            raise
        except Exception as exc:
            error_msg('EXCEPTION: {0}'.format(str(exc)))
            if can_retry:
                progress_msg('   .... SLEEP AND RETRY ....')
                time.sleep(60)
                continue
            raise
    
    if json_data is None or len(json_data.strip()) == 0:
        return None
    return json.loads(json_data.decode("utf-8"))


def get_labels():
	labels = []
	page = 1
	while True:
		new_labels = send_request("labels?direction=asc&page={0}".format(page))
		if not new_labels:
			break
		labels.extend(new_labels)
		page += 1
	return labels

def get_issues_by_labels(labels):
    issues = []
    page = 1
    while True:
        #new_issues = send_request("issues?state=%s&direction=asc&-label=A-Bug&page=%d" % ('open', page))
        #new_issues = send_request('issues?page=%d&q=is:open+is:issue+label:"A-Bug"' % page)
        new_issues = send_request('issues?page=%d&labels=%s' % (page,labels))
        if not new_issues:
            break
        issues.extend(new_issues)
        page += 1
    return issues

if __name__ == '__main__':
    
    #rsps = (send_request('issues'))
    labels = get_labels()
    print(len(labels))
    for label in labels:
        if label['name'] == 'F-Enketo/Webform':
            labels.remove(label)
    
    new_labels = []
    for label in labels:
        new_labels.append(label['name'])
    print(new_labels)
    
    issues = get_issues_by_labels('A-Bug,0 - Backlog')
    print(len(issues))




    
