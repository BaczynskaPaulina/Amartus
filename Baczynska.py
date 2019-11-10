"""
The main goal of this exercise is to write Restful API to 
create, store and retrieve"cards" and display them via web interface.
To be performed with python flask framework

***

Głównym celem tego ćwiczenia jest napisanie Restful API do 
tworzenia, przechowywania i pobierania „kart” oraz wyświetlania ich za pośrednictwem interfejsu WWW.

"""

#http://127.0.0.1:5000/ui/cards

from flask import Flask
from flask import json
from flask import Response
from flask import request
import json

app = Flask(__name__)

class Card():
    
    list_of_cards=[]
    
    def __init__(self, ID, title, content):
        self.ID=ID
        self.title=title
        self.content=content
        
    def create_card():
        #request.method=='PUT'
        title=request.args.get('title')
        content=request.args.get('content')
        ID=request.patch
        obj=Card(ID,title,content)
        list_of_cards.append(obj)
        
        data={}
        data['title']=obj.title
        data['content']=obj.content
        json_data=json.dumps(data)
        
        return json_data
    
    def get_card():
        #request.method=='GET'
        for i in range(len(list_of_cards)):
            pom=list_of_cards[i]
            if pom.ID==request.patch:
                ID=pom.ID
                title=pom.title
                content=pom.content
        obj=Card(ID,title,content)
        
        data={}
        data['title']=obj.title
        data['content']=obj.content
        json_data=json.dumps(data)
        
        return json_data
    
    def list_card():
        #request.method=='GET'
        data={}
        data['items']=[]
        
        for i in range(len(list_of_cards)):
            pom=list_of_cards[i]
            data1={}
            data1['ID']=pom.ID
            data1['title']=pom.title
            data1['content']=pom.content
            json_data=json.dumps(data1)
            data['items'].append(json_data)
            
        json_finaldata=json.dumps(data)
            
        return json_finaldata
            
    def delete_card():
        #request.method=='DELETE'
        for i in range(len(list_of_cards)):
            pom=list_of_cards[i]
            if pom.ID==request.patch:
                list_of_cards.pop(i)
        return
        
    def edit_card():
        #request.method=='PUT'
        new_title=request.args.get('title')
        new_content=request.args.get('content')
        for i in range(len(list_of_cards)):
            pom=list_of_cards[i]
            if pom.ID==request.patch:
                pom.title=new_title
                pom.content=new_content
                ID=pom.ID
                title=pom.title
                content=pom.content
                
                
        obj=Card(ID,title,content)
        
        data={}
        data['title']=obj.title
        data['content']=obj.content
        json_data=json.dumps(data)
        
        return json_data
    
    @app.route('/ui/cards', methods=['PUT','GET','POST','DELETE'])
    def display_all_cards():
        
        json=list_card()
        titles=[]

        for i in range(len(json_dict["items"])):
            pom=json_dict["items"][i]
    
            pom_id=pom["id"]
            ids.append(pom_id)
    
            pom_title=pom["title"]
            titles.append(pom_title)
            
        answer=""
        for i in range(len(json_dict["items"])):
            answer=answer+'''<button type="button">{}</button>'''.format(titles[i])
            
        return answer
    
    @app.route('/ui/cards/<int:id>', methods=['PUT','GET','POST','DELETE'])
    def display_card():
        json=get_card()
        ID=json["id"]
        title=json["title"]
        content=json["content"]
        return '''<h1>ID: {}</h1><h1>Title: {}</h1><h1>Content: {}</h1>'''.format(ID,title,content)
    
    @app.route('/ui/cards', methods=['PUT','GET','POST','DELETE'])
    def metod_switch():
        print("PATH: ",request.path)
        if request.method == 'PUT':
            url=request.path
            url2=url[-4:]
            if url2=="edit":
                a=edit_card(url3,new_title,new_content)
                display_card()
            else:
                a=create_card(title,content)
                display_card()

        elif request.method == 'GET':
            url=request.path
            if url=="/api/pools":
                list_card()
            else:
                get_card()

        elif request.method == 'DELETE':
            delete_card()
            display_all_cards()
            
        else:
            display_all_cards()
        
        

    if __name__ == '__main__':
        app.run(debug=True, port=5000) #run app in debug mode on port 5000
        