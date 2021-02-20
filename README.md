# Thingsboard-CE-device-bulk-upload
Python code that reads from a file and uploads devices to Thingsboard. The code is a part of a script that uploads to both Thingsboard and Chirpstack at the same time. The script relies heavily on a reference code given by thingsboard team.

Make sure to prepare the csv file exactly as it is in the template.
Add your thingsboard URL in the python file, and your thingsboard credentials.

How to run the file:

Run from command prompt:
    Navigate to the folder where the python file is located
    Run python upload_device_tb_ce.py (This will run the script and you should receive a message that devices were created)