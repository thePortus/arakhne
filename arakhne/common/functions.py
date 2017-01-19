import os


def get_env_variable(var_name):     # pragma: no cover
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Required environment variable %s not set" % var_name
        raise Exception(error_msg)
