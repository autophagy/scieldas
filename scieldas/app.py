import logging
from os import environ

import requests
import requests_cache
from flask import Flask, current_app, redirect, render_template, request, url_for
from scieldas.config import config
from scieldas.database import db
from scieldas.models.github_oauth_tokens import GithubOauthTokens, refresh_github_oauth
from scieldas.services import (
    Registry,
    appveyor,
    aur,
    chrome,
    circleci,
    codecov,
    coveralls,
    crates,
    discourse,
    dockerhub,
    github,
    jenkins,
    jetbrains,
    keybase,
    lgtm,
    mastodon,
    misc,
    mozilla,
    npm,
    pepy,
    pypi,
    readthedocs,
    rubygems,
    travis,
)
from sqlalchemy import exc

LOGGER = logging.getLogger(__name__)
REGISTRY = Registry()


def create_application() -> Flask:
    application = Flask(__name__)
    conf = config[environ.get("FLASK_CONFIG", "default")]
    application.config.from_object(conf)  # type: ignore
    db.init_app(application)

    setup_database(application)

    requests_cache.install_cache(
        "scieldas_cache",
        backend="memory",
        expire_after=application.config.get("REQUEST_CACHE_SECONDS"),
    )

    REGISTRY.init_app(application)
    REGISTRY.register("Appveyor", appveyor)
    REGISTRY.register("Arch User Repository", aur)
    REGISTRY.register("Chrome Web Store", chrome)
    REGISTRY.register("CircleCI", circleci)
    REGISTRY.register("Codecov", codecov)
    REGISTRY.register("Coveralls", coveralls)
    REGISTRY.register("Crates.io", crates)
    REGISTRY.register("Discourse", discourse)
    REGISTRY.register("Docker Hub", dockerhub)
    REGISTRY.register("Github", github)
    REGISTRY.register("Jenkins", jenkins)
    REGISTRY.register("Jetbrains", jetbrains)
    REGISTRY.register("Keybase", keybase)
    REGISTRY.register("LGTM", lgtm)
    REGISTRY.register("NPM", npm)
    REGISTRY.register("PePy", pepy)
    REGISTRY.register("PyPi", pypi)
    REGISTRY.register("ReadTheDocs", readthedocs)
    REGISTRY.register("RubyGems", rubygems)
    REGISTRY.register("Travis CI", travis)
    REGISTRY.register("Mastodon", mastodon)
    REGISTRY.register("Mozilla Add-on", mozilla)
    REGISTRY.register("Miscellaneous", misc)
    LOGGER.info(f"Registered services: {REGISTRY.service_count}")

    application.add_url_rule("/", "index", index)
    application.add_url_rule("/_/", "health", health_check)

    application.add_url_rule("/oauth/github", "github_redirect", github_oauth)
    application.add_url_rule(
        "/oauth/github/token", "github_handle", handle_github_oauth
    )
    return application


def index():
    github_thank = request.args.get("github_thank")
    return render_template(
        "index.html",
        github_thank=github_thank,
        services=REGISTRY.registered_categories,
        commit_sha=current_app.config.get("COMMIT_SHA"),
    )


def health_check():
    return "OK"


def setup_database(application: Flask):
    with application.app_context():
        db.create_all()
        seed_token = application.config.get("GITHUB_API_KEY")
        if seed_token:
            try:
                db.session.add(GithubOauthTokens(token=seed_token))
                db.session.commit()
            except exc.IntegrityError:
                LOGGER.debug("Token already present in DB. Skipping...")
                db.session.rollback()
        refresh_github_oauth()


def github_oauth():
    uri = "https://github.com/login/oauth/authorize"
    client = current_app.config.get("GITHUB_CLIENT_ID")
    redirect_uri = f"{request.host_url}oauth/github/token"
    return redirect(f"{uri}?client_id={client}&redirect_uri={redirect_uri}")


def handle_github_oauth():
    code = request.args.get("code")
    resp = requests.post(
        "https://github.com/login/oauth/access_token",
        data={
            "client_id": current_app.config.get("GITHUB_CLIENT_ID"),
            "client_secret": current_app.config.get("GITHUB_CLIENT_SECRET"),
            "code": code,
        },
        headers={"accept": "application/json"},
    )
    with current_app.app_context():
        token = GithubOauthTokens(token=resp.json().get("access_token"))
        db.session.add(token)
        db.session.commit()
    return redirect(url_for("index", github_thank=True))
