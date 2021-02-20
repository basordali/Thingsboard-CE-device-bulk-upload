import logging
import requests
from json import load
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
from tb_rest_client.rest import ApiException
from werkzeug.exceptions import HTTPException, NotFound

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "ENTER YOUR URL"

# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"


# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    try:
        # Auth with credentials
        rest_client.login(username=username, password=password)

        with open('file_test.csv', encoding='utf-8-sig') as file_object: # needed to add encoding type so i can remove weird characters in front of some letters
            try:  
                contents=file_object.read()[89:]#we're reading from the 78th charactrer onwards. this eliminates the very first row
                splitContents=contents.split() #split() breaks down the string at the white spaces and puts the pieces in a set
                for content in splitContents: #looping through the set so we can pick out each piece
                    maxSplit=content.split(',') #removing comma that gets put when we create a set in two rows above
                    devEUI=maxSplit[0]
                    deviceName=maxSplit[1]
                    deviceType=maxSplit[2]
                    description=maxSplit[3]
                    deviceProfileID=maxSplit[4]
                    skipFCntCheck=maxSplit[5]
                    isDisabled=maxSplit[6]
                    applicationID=maxSplit[7]
                    # creating a Device
                    device = Device(name=deviceName, type=deviceType)
                    device = rest_client.save_device(device)
                    logging.info(" Device was created:\n%r\n", device)


    except HTTPException as e:
        logging.exception(e)