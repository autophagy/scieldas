import logging

from flask import current_app
from scieldas.database import db

LOGGER = logging.getLogger(__name__)


class GithubOauthTokens(db.Model):
    token = db.Column(db.String(120), primary_key=True)

    def __repr__(self):
        return f"Token: {self.token}"


def refresh_github_oauth():
    tokens = []
    with current_app.app_context():
        for token in GithubOauthTokens.query.all():
            tokens.append(token.token)
    LOGGER.debug("Refreshing GITHUB_OAUTH_TOKENS to: ")
    LOGGER.debug(f"{len(tokens)} tokens.")
    current_app.config["GITHUB_OAUTH_TOKENS"] = tokens
