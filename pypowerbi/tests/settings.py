class PowerBITestSettings:
    # default testing urls
    authority_url = 'https://login.windows.net/common'
    scopes = ['https://analysis.windows.net/powerbi/api/.default']
    api_url = 'https://api.powerbi.com'

    # testing credentials
    client_id = '00000000-0000-0000-0000-000000000000'
    username = 'someone@somecompany.com'
    password = 'averygoodpassword'
    group_ids = [None, '00000000-0000-0000-0000-000000000000']
