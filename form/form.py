from flask_wtf import Form
from wtforms import TextField, StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError


class UserForm(Form):

   name = StringField("Name", [validators.DataRequired("Please enter your email address."),  validators.length(5, 10, "5 < name < 10.")])

   age = IntegerField("Age Of Student", [validators.DataRequired("Please enter your login."), validators.number_range(0, 100, "Age must be > 0.")])

   submit = SubmitField("Send")