# 🚀 Model Deployment Instructions
## 🖥️ Run the FastAPI Server
#### To deploy the model endpoint locally, use the following command:

`uvicorn deploy_model:app --port 9999`

This will start the server at **http://localhost:9999**


## 📬 Sample POST Request
Use the following **curl** command to send a test request to the **/predict** endpoint:

curl -X 'POST' 'http://localhost:9999/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"duration": 0.0, "protocoltype": "tcp", "service": "private", "flag": "S0", "srcbytes": 0.0, "dstbytes": 0.0, "land": 0.0, "wrongfragment": 0.0, "urgent": 0.0, "hot": 0.0, "numfailedlogins": 0.0, "loggedin": 0.0, "numcompromised": 0.0, "rootshell": 0.0, "suattempted": 0.0, "numroot": 0.0, "numfilecreations": 0.0, "numshells": 0.0, "numaccessfiles": 0.0, "numoutboundcmds": 0.0, "ishostlogin": 0.0, "isguestlogin": 0.0, "count": 123.0, "srvcount": 6.0, "serrorrate": 1.0, "srvserrorrate": 1.0, "rerrorrate": 0.0, "srvrerrorrate": 0.0, "samesrvrate": 0.05, "diffsrvrate": 0.07, "srvdiffhostrate": 0.0, "dsthostcount": 255.0, "dsthostsrvcount": 26.0, "dsthostsamesrvrate": 0.1, "dsthostdiffsrvrate": 0.05, "dsthostsamesrcportrate": 0.0, "dsthostsrvdiffhostrate": 0.0, "dsthostserrorrate": 1.0, "dsthostsrvserrorrate": 1.0, "dsthostrerrorrate": 0.0, "dsthostsrvrerrorrate": 0.0, "lastflag": 19.0}'


Alternatively you can use **Postman** or **Swagger API** assoicated with **FastAPI**. 

#### ✅ Expected Response
The server will process the input and return a prediction or classification result based on the deployed model. The above curl command will return. 

`{"Logistic Reg. attack_type":["neptune"]}`

The key is the model name and the value is the attack type.