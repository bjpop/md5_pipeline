'''
Build the pipeline workflow by plumbing the stages together.
'''

from ruffus import Pipeline, output_from, regex, suffix
from stages import Stages


def make_pipeline(state):
    '''Build the pipeline by constructing stages and connecting them together'''
    # Build an empty pipeline
    pipeline = Pipeline(name='md5')
    # Get a list of paths to all the input files
    input_files = state.config.get_option('files')
    # Stages are dependent on the state
    stages = Stages(state)

    # The original FASTQ files
    # This is a dummy stage. It is useful because it makes a node in the
    # pipeline graph, and gives the pipeline an obvious starting point.
    pipeline.originate(
        task_func=stages.original_files,
        name='original_files',
        output=input_files)

    # Align paired end reads in FASTQ to the reference producing a BAM file
    pipeline.transform(
        task_func=stages.md5_checksum,
        name='md5_checksum',
        input=output_from('original_files'),
        filter=suffix(''),
        output='.md5')


    return pipeline
