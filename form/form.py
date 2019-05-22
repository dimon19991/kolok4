from flask_wtf import Form
from wtforms import TextField, StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError


class UserForm(Form):

   name = StringField("Name", [validators.DataRequired("Please enter your email address.")])

   population = IntegerField("population", [validators.DataRequired("Please enter your login.")])

   submit = SubmitField("Send")