from Server import Flaskserver

app: Flaskserver = Flaskserver()
server = app.server_run()

if __name__ == "__main__":
    server.run(debug=True)
    # server.serve_forever()
