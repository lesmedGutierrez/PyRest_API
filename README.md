# PyRest_API

PyRest_API is a Rest Ful API written in **Python(version 3.6)** that     calculates the intersection ratio (percent of overlap area) between  two shapes and returns a JSON object containing whether the two      polygons intersect or not and if they intersect the ratio of the     intersection.
The App provide two endpoints, one to calculate the    intersect ratio between two squares and another one to calculate the ratio for two circles. One of this figures whether is the square or  circle is fixed in the code(this is a work in progress kind of       thing). To be more especific the square starts its lower left corner at (0, 0) has a width and height of 2; in the other hand the center  of the circle starts at (1, 1) and has a radius of 1. The service for squeare is in **/squareIntersection** and circle in **/circleIntersection**

This small app uses **Flask**, **Flask Restful** and **Shapely** so make sure you have all necesary libraries installed in your system, you can also run pip over the requirements file like this:

    pip install -r requirements.txt

To use this application you can do the following:

    python geometryfull

This is going to start like a web engine that is going to allow us to send a request to our localhost and get a response
To try out the service you can copypaste this line into your browser

> http://localhost:5000/squareIntersection?width=2&height=2&x=1&y=1
> or
> http://127.0.0.1:5000/circleIntersection?radius=2&x=1&y=1

Enjoy :)
