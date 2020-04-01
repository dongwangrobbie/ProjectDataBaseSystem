from flask import Flask, jsonify, request, render_template
from handler.parts import PartHandler
from handler.supplier import SupplierHandler
from handler.customer import CustomerHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')
    # return 'This will be located homepage!'

@app.route('/PartApp/parts', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        # switch to request.json because the form was not working
        # it seems that he was possessed by satanas ...
        # DEBUG to see what the json brings that the customer sends with the new piece
        print("REQUEST: ", request.json)
        # return PartHandler().insertPartJson(request.json)
    else:
        if not request.args:
            return PartHandler().getAllParts()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/PartApp/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getPartById(pid):
    if request.method == 'GET':
        return PartHandler().getPartById(pid)
    elif request.metod == 'PUT':
        return PartHandler().updatePart(pid, request.form)
    elif request.method == 'DELETE':
        return PartHandler().deletePart(pid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/PartApp/parts/<int:pid>/suppliers', methods=['GET', 'POST'])
def getSupplierByPartId(pid):
    return PartHandler().getSupplierByPartId(pid)

@app.route('/PartApp/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)

# This API is to get information of customer by administrator.
@app.route('/PartApp/customers', methods=['GET', 'POST'])
def getALLCustomers():
    if request.method == 'POST':
        return CustomerHandler().insertCustomer(request.form)
    else:
        if not request.args:
            return CustomerHandler().getAllCustomers()
        else:
            return CustomerHandler().searchCustomers(request.args)




if __name__ == '__main__':
    app.run(debug=True)