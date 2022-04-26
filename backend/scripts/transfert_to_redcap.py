"""
script transferant a redcap la liste de patient E-inclusion


"""



from redcap import Project

def prepare_json_data(dic_data):
    json_data = {}


def transfert_data_to_redcap(redcap_url, redcap_key, json_data):
    project = Project(redcap_url, redcap_key, verify_ssl=False)
    response = project.import_records(json_data)
    # print (response)