from flask import Flask, jsonify, request
import os
  
app = Flask(__name__)
  
@app.route('/', methods=['GET'])

 
def helloworld():
    if os.environ['MESSAGE'] == None:
        message = 'Hello world !'
    else:
        message = os.environ['MESSAGE']

    if(request.method == 'GET'):
        data = {"message": message}
        return jsonify(data)
  
if __name__ == '__main__':    
    if os.environ['PORT'] == None:
        port = 5555
    else:
        port = int(os.environ['PORT'])
        
    app.run(host="0.0.0.0", port=port)