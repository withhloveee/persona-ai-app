from core.db import Users
from tools.helpers import reset_daily_tokens


def validate_user(user_id, reset_tokens=False):
    user = Users.query.filter_by(id=user_id).first()
    
    if not user:
        return None, {"Error": "User not found."}
    
    if reset_tokens:
        reset_daily_tokens(user)

    if user.daily_tokens_used >= user.daily_token_limit:
        return None, ({"Error": "Out of Token's for today."}, 429)

    return user, None
