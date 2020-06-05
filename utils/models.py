import string


class SuiteConfig:
    """
    Support Suite Configuration Class
    Available data:
    * base_url: string | The base url of all calls to be done. Optional. Default is an empty string for easier concat
    * enabled: true or false. Default: True | Whether the suite must be executed or not
    """
    def __init__(self, base_url='', enabled=True):
        self.base_url = base_url
        self.enabled = enabled

    @classmethod
    def from_config(cls, config_object):
        base_url = config_object.get('baseUrl')
        enabled = config_object.get('enabled')
        return cls(base_url=base_url, enabled=enabled)
