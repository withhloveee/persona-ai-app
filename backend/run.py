from main import app

# registring routes
import core.routes.auth
import core.routes.stream

if __name__ == '__main__':
    app.run(debug=True,port=8000)