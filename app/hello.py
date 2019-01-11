from flask import render_template, flash, redirect, url_for, request
from app import app
import app.forms as Forms
from app import client
@app.route('/')
@app.route('/index')
def index():

    data=client.refresh()
    return render_template('index.html',title='Home', data=data)



@app.route('/device/<name>', methods=['GET', 'POST'])
def device(name=0):
    form = Forms.addDevice()
    data=client.refresh()
    if request.method=="POST":
        #if form.validate==True:
        print("Przyjeto")
        form.name.data=name
        client.sendTo(form.getDict())
        return redirect(url_for('device', name=0))
    return render_template('device.html',title='Home', data=data, form=form, name=name)

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
    #device={"name": "", "desc": "", "typeName": "", "refreshTime": "", "isRec": False}
    form = Forms.addDevice()
    
    if form.validate_on_submit():
        client.sendTo(form.getDict())
        return redirect(url_for('device', name=0))
    return render_template('addDevice.html', title='Sign In', form=form)

@app.route('/adddev/<dev>', methods=['GET', 'POST'])
def addDev2(dev):
    data=client.refresh()
    print("aaaaaaaaaaaa")
    form = Forms.addDevice()
    #form.PreWrite(data["dicDev"][dev])
    if form.validate_on_submit():
        print("KeyWasPressed")
        client.sendTo(form.getDict())
        return redirect(url_for('device'))
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
    form.setChoices(client.refresh())
    if form.validate_on_submit():
        client.sendTo(form.getDict())
        return redirect(url_for('index'))
    return render_template('addSmall.html', title='Sign In', form=form)

@app.route('/addeffect', methods=['GET', 'POST'])
def addEffect():
    form = Forms.addEffect()
    form.setChoices(client.refresh())
    if form.validate_on_submit():
        client.sendTo(form.getDict())
        return redirect(url_for('index'))
    return render_template('addEffect.html', title='Sign In', form=form)

@app.route('/cam/<ip>')
def cam(ip='0'):
    data=client.refresh()
    return render_template('cam.html',title='Cameras', data=data, ip=ip)

@app.route('/data')
def dataStr():
    data=client.refresh()
    return render_template('dataStr.html',title='data',strin=str(data))