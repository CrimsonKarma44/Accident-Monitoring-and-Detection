import json

LOCATION = "./storage/store.json"

class JsonHandler:
   def load() -> list:
      with open(LOCATION, "r") as file:
         content = json.loads(file.read())
         return content

   def save(value:dict) -> None:
      content = JsonHandler.load()
      content.append(value)
      
      with open(LOCATION, "w") as file:
         json.dump(content, file)
         
   def save2(value:dict) -> None:      
      content = JsonHandler.load()
      content.append(value)
      with open(LOCATION, "w") as file:
         json.dump(content, file)
      
