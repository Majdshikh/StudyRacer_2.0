from bottle import redirect, route, run, error, template, request, static_file, redirect


@route("/")
def user_logged_in():
    userLoggedIn = True

    return template("index", userLoggedIn=userLoggedIn)

@error()
def error(error):
    """
    Hanterar: Error 404 filen hittades inte.
    """

    return template("error")

@route("/static/<filename>")
def static_files(filename):

    return static_file(filename, root="static")


run(host="127.0.0.1", port=8080, reloader=True, debug=True)
