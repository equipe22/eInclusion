"""
script interrogeant redcap sur le nom d'un projet et le transmettant a la DB

"""

class redcap_api_request:
    def __init__(self, redcap_url):
        self.redcap_url = redcap_url