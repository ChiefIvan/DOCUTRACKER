from Server import Flaskserver

app = Flaskserver()

if __name__ == "__main__":
    app.server_run().run(debug=True)
    # app.server_run().serve_forever()
