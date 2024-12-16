from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.exceptions import BadRequest

user_purchase = Blueprint('user_purchase', __name__)