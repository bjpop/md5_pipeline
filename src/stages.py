'''
Individual stages of the pipeline implemented as functions from
input files to output files.

The run_stage function knows everything about submitting jobs and, given
the state parameter, has full access to the state of the pipeline, such 
as config, options, DRMAA and the logger.
'''

from utils import safe_make_dir
from runner import run_stage
import os

class Stages(object):
    def __init__(self, state):
        self.state = state

    def original_files(self, output):
        '''Original input files'''
        pass

    def md5_checksum(self, file_in, md5_out):
        '''Compute the md5 checksum for a file'''
        command = 'openssl md5 {file_in} > {md5_out}'.format(file_in=file_in, md5_out=md5_out)
        run_stage(self.state, 'md5_checksum', command)

