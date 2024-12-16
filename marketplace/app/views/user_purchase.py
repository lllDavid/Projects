from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.exceptions import BadRequest

from marketplace.app.user.user_creator import UserCreator
from marketplace.helpers.validation import validate_user_input

user_purchase = Blueprint('user_purchase', __name__)