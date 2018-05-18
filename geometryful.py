from flask import Flask, request
from flask_restful import Resource, Api
from shapely.geometry import Point, Polygon

app = Flask(__name__)
api = Api(app)


class SquareIntersection(Resource):
    def __init__(self):
        pos = [(0, 0), (0, 2), (2, 2), (2, 0)]
        self.square_default = Polygon(pos)

    def get(self):
        width = float(request.args.get('width', '0'))
        height = float(request.args.get('height', '0'))
        x = float(request.args.get('x', '0'))
        y = float(request.args.get('y', '0'))
        pos = [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]
        square = Polygon(pos)
        if square.intersection(self.square_default).area > 0.0:

            return {'intersec': 'yes',
                    'ratio': (square.intersection(self.square_default).area)/(square.area)}
        else:
            return {'intersec': 'no', 'ratio': 0.0}


class CircleIntersection(Resource):
    def __init__(self):
        self.circle_default = Point(1, 1).buffer(1)

    def get(self):
        radius = float(request.args.get('radius', '0'))
        x = float(request.args.get('x', '0'))
        y = float(request.args.get('y', '0'))
        circle = Point(x, y).buffer(radius)
        if circle.intersects(self.circle_default):
            intersection_area = circle.intersection(self.circle_default).area
            return {'intersec': 'yes',
                    'ratio': intersection_area/(circle.area)}
        else:
            return {'intersect': 'no',
                    'ratio': 0.0}

api.add_resource(SquareIntersection, '/square')
api.add_resource(CircleIntersection, '/circle')

if __name__ == '__main__':
    app.run(debug=True)