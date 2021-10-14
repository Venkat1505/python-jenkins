#!/usr/bin/env python

import os, shutil, sys, argparse, re
import utils, paths
import boto
import math, os


from boto.s3.connection import S3Connection
conn = S3Connection('AKIAY4NJCOQ34ZC7VKG3', 'po9oABJQNDVcnql0Hq+b1y9AjOS0OsKNM+RNsMOC')
bucket = conn.get_bucket('interpreta-build-storage','releases')


def uploadBuilds():
     print('In uploadBuilds')

  uploadBuilds()
