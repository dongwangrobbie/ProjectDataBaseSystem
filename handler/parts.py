from flask import jsonify
from dao.parts import PartsDAO

class PartHandler:
    def build_part_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['res_type'] = row[1]
        result['unit_price'] = row[2]
        return result

    def build_part_attributes(self, res_id, res_type, unit_price):
        result = {}
        result['resource_id'] = res_id
        result['res_type'] = res_type
        result['unit_price'] = unit_price
        return result

    def getAllParts(self):
        dao = PartsDAO()
        parts_list = dao.getAllParts()
        result_list = []
        for row in parts_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

    def getPartById(self, pid):
        dao = PartsDAO()
        row = dao.getPartById(pid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            part = self.build_part_dict(row)
            return jsonify(Part=part)

    def searchParts(self, args):
        dao = PartsDAO

    def deletePart(self, pid):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error="Part Not Found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus="OK"), 200

    def updatePart(self, pid, form):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error="Part Not Found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Column Amount in Malform."), 400
            else:
                res_type = form['res_type']
                unit_price = form['unit_price']
                if res_type and unit_price:
                    dao.update(pid, res_type, unit_price)
                    result = self.build_part_attributes(pid, res_type, unit_price)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected Attributes for Update Request."), 400




