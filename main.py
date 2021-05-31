from website import create_app

app = create_app()

# run webserver#

if __name__ == '__main__':
    app.run(debug=True)  # any change will rerun the webserver#
