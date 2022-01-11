import mypythontools

# All the parameters can be overwritten via CLI args
mypythontools.utils.push_pipeline(
    tests=False, version=None, sphinx_docs=False, deploy=True
)
