from flask import Flask, jsonify, request
import time, requests, os
from jose import jwt

# Backend dùng tên nội bộ Docker để fetch JWKS (port 8080)
_INTERNAL = os.getenv("OIDC_INTERNAL", "http://authentication-identity-server:8080")
REALM     = os.getenv("OIDC_REALM",    "realm_52300263")
AUDIENCE  = os.getenv("OIDC_AUDIENCE", "account")
JWKS_URL  = f"{_INTERNAL}/realms/{REALM}/protocol/openid-connect/certs"

_JWKS = None; _TS = 0
def get_jwks():
    global _JWKS, _TS
    now = time.time()
    if not _JWKS or now - _TS > 600:
        _JWKS = requests.get(JWKS_URL, timeout=5).json()
        _TS = now
    return _JWKS

app = Flask(__name__)

@app.get("/hello")
def hello(): return jsonify(message="Hello from App Server!")

@app.get("/secure")
def secure():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify(error="Missing Bearer token"), 401
    token = auth.split(" ", 1)[1]
    try:
        # options: bỏ verify_iss vì Keycloak ký với localhost:8081
        # nhưng vẫn verify signature (RS256) và audience
        payload = jwt.decode(
            token,
            get_jwks(),
            algorithms=["RS256"],
            audience=AUDIENCE,
            options={"verify_iss": False}
        )
        return jsonify(
            message="✅ Secure resource OK!",
            preferred_username=payload.get("preferred_username"),
            email=payload.get("email")
        )
    except Exception as e:
        return jsonify(error=str(e)), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)