#this script is a prototype, and very specific. As always it should be executed on aproduction env only after thourough testing.
#This script functions as a way to search all sashboards by associated API key searching for the Orginization ID by name

# usage python3 main.py -k <api key> -o <specific org name>

import requests

def main(argv):
    global arg_apikey
    global m_baseUrl

    arg_apikey = None
    arg_orgname = None

    try:
        opts, args = getopt.getopt(argv, 'k:o:m:')
    except getopt.GetoptError:
        sys.exit(0)

    for opt, arg in opts:
        if opt == '-k':
            arg_apikey = arg
        elif opt == '-o':
            arg_orgname = arg


    if arg_apikey is None or arg_orgname is None:
        print('Please specify the required values!')
        sys.exit(0)

    # set needed vlaues from env_vars
    m_headers = {'X-Cisco-Meraki-API-Key': arg_apikey}
    m_baseUrl = 'https://api.meraki.com/api/v1'

    timenow = datetime.datetime.now()

    # get orgid for specified org name
    org_response = requests.request("GET", f'{m_baseUrl}/organizations/', headers=m_headers)
    org = org_response.json()
    for row in org:
        if row['name'] == arg_orgname:
            orgid = row['id']
            print("Org" + " " + row['name'] + " " + "found.")
        else:
            print("Exception: This Org does not match:" + ' ' + row['name'] + ' ' + 'Is not the orginization specified!')