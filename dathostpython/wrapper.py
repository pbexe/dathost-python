import json
import requests

class dathost:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw
    def servers(self):
        data = requests.get('https://dathost.net/api/0.1/game-servers', auth=requests.auth.HTTPBasicAuth(self.user, self.passw))
        return json.loads(data.text)
    def duplicate(self, template):
        data = requests.post('https://dathost.net/api/0.1/game-servers/' + template + '/duplicate',auth=(self.user, self.passw))
        return json.loads(data.text)
    def delete(self, _id):
        url = 'https://dathost.net/api/0.1/game-servers/' + _id
        data = requests.delete(url, auth=(self.user, self.passw))
        return json.loads(data.text)
    def getFile(self, _id, path):
        data = requests.get('https://dathost.net/api/0.1/game-servers/' + _id + "/files/" + path, auth=requests.auth.HTTPBasicAuth(self.user, self.passw))
        return data.text
    def start(self, _id):
        data = requests.post('https://dathost.net/api/0.1/game-servers/' + _id + '/start', auth=(self.user, self.passw))
        return json.loads(data.text)
    def stop(self, _id):
        data = requests.post('https://dathost.net/api/0.1/game-servers/' + _id + '/stop', auth=(self.user, self.passw))
        return json.loads(data.text)
    def upload(self, _id, path, files):
        data = requests.post('https://dathost.net/api/0.1/game-servers/' + _id + '/stop', files=files, auth=(self.user, self.passw))
        return data
    def info(self, _id):
        data = requests.get('https://dathost.net/api/0.1/game-servers/' + _id, auth=requests.auth.HTTPBasicAuth(self.user, self.passw))
        return json.loads(data.text)
