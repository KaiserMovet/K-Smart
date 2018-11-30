from flask import render_template, flash, redirect, url_for
from app import app
import app.forms as Forms
from app import client
@app.route('/')
@app.route('/index')
def index():

    data=client.refresh()
    return render_template('index.html',title='Home', data=data)



@app.route('/device')
def device():

    data=client.refresh()
    return render_template('device.html',title='Home', data=data)

@app.route('/cond')
def cond():

    data=client.refresh()
    return render_template('cond.html',title='Home', data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/adddev', methods=['GET', 'POST'])
def addDev():
    form = Forms.addDevice()
    if form.validate_on_submit():
        client.sendTo(form.getDict())
        return redirect(url_for('index'))
    return render_template('addDevice.html', title='Sign In', form=form)

@app.route('/addcon', methods=['GET', 'POST'])
def addCon():
    form = Forms.addCon()
    if form.validate_on_submit():
        client.sendTo(form.getDict())
        return redirect(url_for('index'))
    return render_template('addCon.html', title='Sign In', form=form)

@app.route('/addsmall', methods=['GET', 'POST'])
def addSmall():
    form = Forms.addSmall()
    if form.validate_on_submit():
        client.sendTo(form.getDict())
        return redirect(url_for('index'))
    return render_template('addSmall.html', title='Sign In', form=form)

@app.route('/addeffect', methods=['GET', 'POST'])
def addEffect():
    form = Forms.addEffect()
    if form.validate_on_submit():
        client.sendTo(form.getDict())
        return redirect(url_for('index'))
    return render_template('addEffect.html', title='Sign In', form=form)