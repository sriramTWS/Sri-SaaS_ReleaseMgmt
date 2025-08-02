import flask
from flask import request, jsonify
import pymongo
from pymongo import collection
from pymongo import MongoClient
import os

myclient = MongoClient("mongodb+srv://mongouser:mongouser@cluster0-31gzu.mongodb.net/AssetMgmtDB?retryWrites=true&w=majority")
db = myclient.AssetMgmtDB

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Asset Management Workbench</h1><p>This site is a prototype API for UnO Use Cases</p>"

Leave ={
  "InterfaceName": "GenerateAssetJournals",
  "RequestParameters": [
    {
      "Name": "LedgerId",
      "Value": "2021"
    },
    {
      "Name": "AssetBook",
      "Value": "CORPORATE"
    }
  ]
}


@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/AssetNumber/10100', methods=['GET'])
def assetsinOracleFusion():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.AssetNumber" : "10100"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
@app.route('/maxrest/rest/mbo/ASSET/10100/action=MAINT', methods=['GET'])
def place_assetin_maintmode_maximo():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"STATUS" : "MAINT"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 

@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/300000045689822', methods=['GET'])
def place_assetin_maintmode_oraclefusion():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"Location" : "MAINTENANCE DEPOT"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 

@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/CIP101', methods=['GET'])
def get_cip_fixed_asset():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.AssetNumber" : "CIP101"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})  

@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/captizationofAssets', methods=['GET'])
def get_asset_byAssetID_oraclefusion():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.AssetType" : "Capitalized"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 

@app.route('/fscmRestApi/resources/11.13.18.05/journals/JournalCategoryCode/Asset', methods=['GET'])
def generate_accounting_entries_oraclefusion():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.JournalBatchName" : "CAPITALIZATION_CIP101"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 
     
@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/PLT-9901', methods=['GET'])
def get_fixed_asset():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.AssetNumber" : "PLT-9901"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 
     
@app.route('/fscmService/AssetRetirementsService/WSDL', methods=['GET'])
def retire_asset():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"RetirementId" : "300000123456789"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})

@app.route('/fscmRestApi/resources/11.13.18.05/CreateAccounting', methods=['GET'])
def create_accounting():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"InterfaceName" : "CreateAccounting"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 

@app.route('/fscmRestApi/resources/11.13.18.05/journals/JournalSourceCode/Assets/AccountingDate/20240526', methods=['GET'])
def create_retirement_journalentries():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.JournalBatchName" : "RETIREMENT_PLT9901"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})  

@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/AssetNumber/300000099821456', methods=['GET'])
def set_status_retired():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.AssetStatus" : "Retired"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 
     
     
@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/yardauction/AssetNumber/PLT-9901', methods=['GET'])
def asset_eligibility_test_auction():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.Location" : "Yard-Auction"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
  
@app.route('/auction/items', methods=['GET'])
def auction_items():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"auctionItemId" : "AUC-55431"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
     
@app.route('/auction/events/EVT-20240527/items/AUC-55431/submit', methods=['GET'])
def push_asset_to_auction_platform():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"eventId" : "EVT-20240527"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/assettransferstatus/AssetNumber/FCL-2023-8801', methods=['GET'])
def get_asset_transfer_status():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"items.0.TransferStatus": "None"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/3000001992022/updateownership', methods=['GET'])
def update_ownership_in_OracleFusion():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"Message": "Ownership and location updated successfully."}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
@app.route('/maximo/oslc/os/mxasset/_QVNTRVROVU1fPVwiRkNMLTIwMjMtODgwMVwi', methods=['GET'])
def update_ownership_in_maximo():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"status" : "TRANSFERRED"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
@app.route('/api/now/table/sc_task', methods=['GET'])
def trigger_asset_movment_notifications():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"result.number": "TASK0059203"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})
     
@app.route('/fscmRestApi/resources/11.13.18.05/fixedAssets/completed/3000001992022', methods=['GET'])
def confirm_transfer():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"TransferStatus" : "Completed"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})

@app.route('/maximo/oslc/os/auditlog', methods=['GET'])
def maximo_audit_record_retired_asset():
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"event" : "RETIREMENT_ARCHIVE"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test})

     
     
     
@app.route('/fscmRestApi/resources/11.13.18.05/erpintegrations', methods=['POST'])
def put_data():
     NewCol = db.AssetMgmtDB
     post = [ {
  "InterfaceName": "GenerateAssetJournals",
  "RequestParameters": [
    {
      "Name": "LedgerId",
      "Value": "2021"
    },
    {
      "Name": "AssetBook",
      "Value": "CORPORATE"
    }
  ]
}

]
     result = NewCol.insert_many(post)
     NewCol = db.AssetMgmtDB
     result = NewCol.find({})
     print(result)
     output=[]
     test=dict(NewCol.find_one({"InterfaceName": "GenerateAssetJournals"}))
     del test["_id"]
     print(test)
     return jsonify({'result' : test}) 

app.run(host="0.0.0.0", port=5000)
