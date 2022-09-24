import json
import os.path

def displayAllBooks(books):
    print("")
    for current_book in books:
        for current_key in current_book:
            print(current_key,":",current_book[current_key])

def getNumericInput(displayString):
    while(True):
        user_data = input(displayString)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("Please insert a NUMBER")

def addBook():
    book = {
            "title":"",
            "num_of_pages": 0,
            "language":"",
            "author":"",
            "publishing_year":0,
            "last_time_read": {
                "day" : 0,
                "month":"",
                "year" : 0
            },
            "chapters" : []
            }

    book["title"] = input("Please insert the title:")
    book["num_of_pages"] = getNumericInput("Please insert the number of pages:")
    book["language"]= input("Please insert the language:")
    book["author"]= input("Who is the author:")
    book["publishing_year"] = getNumericInput("Please insert the year of publishing:")
    last_time_read = input ("When did you last read this book?: Please insert date with the format: DD/MM/YYYY")
    last_time_read = last_time_read.split("/")
    book["last_time_read"]["day"] = int (last_time_read[0])
    book["last_time_read"]["month"] = last_time_read[1]
    book["last_time_read"]["year"] = int(last_time_read[2])
    while(True):
        chapter = input("please insert a chapter to the book; insert END to finish")
        if (chapter == "END"):
            break
        else:
            book["chapters"].append(chapter)
    return book

def loadExistingBooks():
    if(os.path.exists("books.json")):
        with open('books.json') as file_data:
            print(file_data)
            books = json.load(file_data)
            return books
    else:
        return []

def saveToTheFile(books):
    f = open("books.json","w")
    print(books)
    f.write(json.dumps(books,indent=2))
    f.close()

def main():

    books = []
    books= loadExistingBooks()

    while(True):
        insert_mode = input("Do you want to start adding books?, Answer yes or no")
        if(insert_mode == "no"):
            print("Good bye")
            break
        else:
            book = addBook()
            books.append(book)

    print("Saving to the file ")
    saveToTheFile(books)
    displayAllBooks(books)

///
var radiusM = prompt("Select the radius in meters");
var angleDeg = prompt("Select the angle in degrees");
var dot;
var p1;
var p2;
var pixelUnit;
var radiusPixel;
var yCrd;
var xCrd;

L.CanvasOverlay = L.Layer.extend({
 
    initialize: function (userDrawFunc, options) {
        this._userDrawFunc = userDrawFunc;
        L.setOptions(this, options);
    },

    drawing: function (userDrawFunc) {
        this._userDrawFunc = userDrawFunc;
        return this;
    },

    params: function(options){
        L.setOptions(this, options);
        return this;
    },
  
    onAdd: function (map) {
        this._map = map;
        this._canvas = L.DomUtil.create('canvas', 'leaflet-heatmap-layer');

        var size = this._map.getSize();
        this._canvas.width = size.x;
        this._canvas.height = size.y;

        map._panes.overlayPane.appendChild(this._canvas);
        map.on('moveend', this._reset, this);
        map.on('resize',  this._resize, this);
        this._reset();
    },

    addTo: function (map) {
        map.addLayer(this);
        return this;
    },

    _resize: function (resizeEvent) {
        this._canvas.width  = resizeEvent.newSize.x;
        this._canvas.height = resizeEvent.newSize.y;
    },

    _reset: function () {
        var topLeft = this._map.containerPointToLayerPoint([0, 0]);
        L.DomUtil.setPosition(this._canvas, topLeft);
        this._redraw();
    },

    _redraw: function () {
        var size     = this._map.getSize();
        var bounds   = this._map.getBounds();
        var zoomScale = (size.x * 180) / (20037508.34  * (bounds.getEast() - bounds.getWest())); // resolution = 1/zoomScale
        var zoom = this._map.getZoom();
     
        if (this._userDrawFunc) {
            this._userDrawFunc(this,
                                {
                                    canvas   : this._canvas,
                                    bounds   : bounds,
                                    size     : size,
                                    zoomScale: zoomScale,
                                    zoom : zoom,
                                    options: this.options
                                });
        }

        this._frame = null;
    }
});

L.canvasOv = function (userDrawFunc, options) {
    return new L.CanvasOverlay(userDrawFunc, options);
};

L.canvasOv()
    .drawing(sector)
    .params({location: [40.192184088929636, 44.50438089549554], color: "rgba(76, 104, 65, 0.3)", fillColor: "rgba(76, 104, 65, 0.3)", radius: radiusM, angle: angleDeg})
    .addTo(map);

function sector(canvasOv, params) {
    var half_ang_rad = params.options.angle * Math.PI / 360;
    var ctx = params.canvas.getContext('2d');
    ctx.clearRect(0, 0, params.canvas.width, params.canvas.height);
    ctx.fillStyle = params.options.fillColor;
    ctx.strokeStyle = params.options.color;
    if (params.bounds.contains([params.options.location[0], params.options.location[1]])) {
        dot = canvasOv._map.latLngToContainerPoint([params.options.location[0], params.options.location[1]]);
        p1 = canvasOv._map.containerPointToLatLng([0, 0]);
        p2 = canvasOv._map.containerPointToLatLng([0, 1]);
        pixelUnit = canvasOv._map.distance(p1, p2);
        radiusPixel = radiusM / pixelUnit;
        yCrd = radiusPixel * Math.sin(half_ang_rad);
        xCrd = radiusPixel * Math.cos(half_ang_rad);

        ctx.beginPath();
        ctx.moveTo(dot.x, dot.y);
        ctx.lineTo(dot.x + xCrd, dot.y - yCrd);
        ctx.arc(dot.x, dot.y, radiusPixel, 2 * Math.PI - half_ang_rad, half_ang_rad, false);
        ctx.lineTo(dot.x, dot.y);
        ctx.stroke();    
        ctx.fill();
        ctx.closePath();
    }
};



///
main()
