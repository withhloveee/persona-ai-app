from authlib.integrations.flask_client import OAuth
from flask import redirect, url_for
from main import app, db
from core.db import Users
from flask_jwt_extended import create_access_token
from urllib.parse import urlencode

oauth = OAuth(app)

oauth.register(
    name="google",
    client_id=app.config["GOOGLE_CLIENT_ID"],
    client_secret=app.config["GOOGLE_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile"
    }
)

@app.route("/login/google")
def google_login():
    redirect_uri = url_for(
        "google_authorize",
        _external=True
    )
    return oauth.google.authorize_redirect(
        redirect_uri
    )

@app.route("/authorize/google")
def google_authorize():

    token = oauth.google.authorize_access_token()

    user_info = token.get("userinfo") or oauth.google.userinfo(token=token)

    google_id = user_info["sub"]
    email = user_info["email"]

    user = Users.query.filter_by(google_id=google_id).first()

    if not user:
        user = Users(
            google_id=google_id,
            username=email
        )

        db.session.add(user)
        db.session.commit()

    jwt_token = create_access_token(identity=str(user.id))
    frontend_url = app.config["FRONTEND_URL"].rstrip("/")
    query = urlencode({
        "token": jwt_token,
        "user": user_info.get("name") or user.username
    })

    return redirect(f"{frontend_url}/auth/callback?{query}")
