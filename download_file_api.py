import requests

# Cycle Log_022.zip   Test_#1_CycleLog.zip
my_server = "http://14.225.207.9:1991/get_file"
query_param = {"filename": "Test_#1_CycleLog.zip"}

response = requests.get(my_server, params=query_param)

with open("test_file_2.zip", mode="wb") as file:
    file.write(response.content)

print("Response: " + str(response.status_code))

