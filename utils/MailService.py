from MailTMClient import MailTMClient
import json
TOKEN_FILE = "token.json"
TOKEN = None

class MailService():
    def __init__(self):
        TOKEN = self.loadTokenFromFile()
        self.Client = MailTMClient(token=TOKEN)
        
        pass
    
    def saveTokenToFile(self,token: str):
        with open(TOKEN_FILE, "r+") as j:
            contents = json.loads(j.read())
            contents["token"] = token
            j.seek(0)
            j.write(json.dumps(contents, indent=4))
            j.truncate()


    def loadTokenFromFile(self,):
        with open(TOKEN_FILE, "r+") as j:
            contents = json.loads(j.read())
            if len(contents["token"]) > 10:
                return contents["token"]
            else:
                return False


    def clearTokenFile(self,):
        with open(TOKEN_FILE, "w") as j:
            j.write(json.dumps({"token": ""}, indent=4))

    
    def check_inbox(self) -> list:
        MailList = []
        inbox = (self.Client.getInbox())[::-1]
        if len(inbox) >= 1:
            for index, email in enumerate(inbox):
                MailList.append(
                    {
                        'id' : str(index + 1),
                        'subject' : email.subject,
                        'from':email.fromAddress
                    }
                )
            return MailList
        else:
            return MailList
    
    def read_mail(self,index_mail:int) -> list:
        MailList = []
        inbox = self.Client.getInbox()
        for index, email in enumerate(inbox):
            if int(index + 1) == int(index_mail):
                MailList.append(
                    {
                        'subject':email.subject,
                        'from':email.fromAddress,
                        'to':", ".join(email.toAddress),
                        'text':email.text
                    }
                )
        return MailList
    
    def delete_mail(self,index_index:int):
        inbox = self.Client.getInbox()
        for index, email in enumerate(inbox):
            if int(index + 1) == int(index_index):
                res = email.delete()
                if res == 0:
                    return True
                if res == 1:
                    return False
        return False
    
    def logout(self):
        self.clearTokenFile()
    