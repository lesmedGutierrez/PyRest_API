from flask import Flask, request
from flask_restful import Resource, Api
from shapely.geometry import Point, Polygon

app = Flask(__name__)
api = Api(app)


class SquareIntersection(Resource):

    def __init__(self):
#       Initialize default square to compare later
        pos = [(0, 0), (0, 2), (2, 2), (2, 0)]
        self.square_default = Polygon(pos)

#   function that will be called when there"s a get call in the resource
    def get(self):
        width = floatParser(request.args.get("width", "0"))
        height = floatParser(request.args.get("height", "0"))
        x = floatParser(request.args.get("x", "0"))
        y = floatParser(request.args.get("y", "0"))
        res = True
        if width<=0 or height<=0:
            res = {"Error": "Invalid Input. width and height must be positive integers of floats"}
        elif width and height and x and y:
            pos = [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]
            # Square that is drawn to be compared with square_default
            # to see if they intersect and if so which is the ratio
            square = Polygon(pos)
            if square.intersection(self.square_default).area > 0.0:
                res = {"intersec": "yes",
                        "ratio": (square.intersection(self.square_default).area)/(square.area)}, 201
            else:
                res = {"intersec": "no", "ratio": 0.0}
        else:
            res = {"Error": "Invalid Input. Make sure width, height, x, y are integers or floats"}, 201
        return res


class CircleIntersection(Resource):
    #       Initialize default square to compare later
    def __init__(self):
        self.circle_default = Point(1, 1).buffer(1)

    #   function that will be called when there"s a get call in the resource
    def get(self):
        radius = floatParser(request.args.get("radius", ""))
        x = floatParser(request.args.get("x", ""))
        y = floatParser(request.args.get("y", ""))
        res = True
        if radius <= 0:
           res = {"Error": "Invalid Input. Radius must be positive integer or float"}, 201
        elif radius and x and y:
            circle = Point(x, y).buffer(radius)
            if circle.intersects(self.circle_default):
                intersection_area = circle.intersection(self.circle_default).area
                res = {"intersec": "yes",
                        "ratio": intersection_area/(circle.area)}
            else:
                res = {"intersect": "no",
                        "ratio": 0.0}
        else:
            res = {"Error": "Invalid Input. Make sure radius, x, y are integers or floats"}, 201
        return res

def floatParser(value):
    try:
        value = float(value)
    except ValueError:
        value = False
    return value



class HaciendaRespAsincrona(Resource):

    def __init__(self):
        pass

    def post(self):
        print(request.get_json(force=True))
        print(request.get_data())
        res = request.get_json(force=True) or dict()
        res['method'] = request.method
        return res, 200

    def get(self):
        print(request.get_json(force=True))
        print(request.get_data())
        res = request.get_json(force=True) or dict()
        res['method'] = request.method
        return res, 200


class Trafico(Resource):

    def __init__(self):
        super(Trafico, self).__init__()

    def post(self):
        print(request.get_json(force=True))
        print(request.get_data())
        res = request.get_json(force=True) or dict()
        res['method'] = request.method
        res = {"el que lee esto": "es gay"}
        return res, 200

    def get(self):
    #     print(request.get_json(force=True))
    #     print(request.get_data())
    #     res = request.get_json(force=True) or dict()
    #     res['method'] = request.method
        res = {"el que lee esto": "es gay"}
        return res, 200




api.add_resource(SquareIntersection, "/squareIntersection")
api.add_resource(CircleIntersection, "/circleIntersection")
api.add_resource(HaciendaRespAsincrona, "/hacienda")
api.add_resource(Trafico, "/trafico")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2552)

