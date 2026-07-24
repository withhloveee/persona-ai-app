from datetime import date
from core.db import db

with open("core/routes/rules/prompt.txt", "r", encoding="utf-8") as f:
    DEFAULT_PROMPT = f.read()

with open("core/routes/rules/summary.txt", "r", encoding="utf-8") as f:
    SUMMARY_PROMPT = f.read()

with open("core/routes/rules/senjougahara.txt", "r", encoding="utf-8") as f:
    senjougahara_overview = f.read()
    
with open("core/routes/rules/fern.txt", "r", encoding="utf-8") as f:
    fern_overview = f.read()
    
with open("core/routes/rules/hayasaka.txt", "r", encoding="utf-8") as f:
    hayasaka_overview = f.read()
    

# HELPER fn: for token reset.
def reset_daily_tokens(user):
    today = date.today()

    print(today)
    if user.last_token_reset != today:
        user.daily_tokens_used = 0
        user.last_token_reset = today
        db.session.commit()