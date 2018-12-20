from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class addDevice(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    desc = StringField('desc', validators=[DataRequired()])
    typeName = StringField('typeName', validators=[DataRequired()])
    refreshTime = IntegerField('refreshTime',validators=[NumberRange(min=-1, max=255)])
    isRec=BooleanField('isRec')
    submit = SubmitField('Save')
    def getDict(self):
        
        mess=dict()
        mess["exe"]="addDev"
        mess["name"]=self.name.data
        mess["desc"]=self.desc.data
        mess["typeName"]=self.typeName.data
        mess["refreshTime"]=self.refreshTime.data
        mess["isRec"]=self.isRec.data
        return mess


class addCon(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    desc = StringField('desc', validators=[DataRequired()])
    refreshTime = IntegerField('refreshTime',validators=[NumberRange(min=-1, max=255)])
    submit = SubmitField('Save')

    def getDict(self):
        mess=dict()
        mess["exe"]="addCon"
        mess["name"]=self.name.data
        mess["refreshTime"]=self.refreshTime.data
        mess["desc"]=self.desc.data
        return mess

class addEffect(FlaskForm):
    conName = StringField('conName', validators=[DataRequired()])
    effectName = StringField('effectName', validators=[DataRequired()])
    deviceName = StringField('deviceName', validators=[DataRequired()])
    trueValue = IntegerField('trueValue',validators=[NumberRange(min=-1, max=255)])
    falseValue = IntegerField('falseValue',validators=[NumberRange(min=-1, max=255)])
    submit = SubmitField('Save')

    def setChoices(self,data):
        self.conName.choices=[(name,name) for name in data["dicCon"].keys()]
        self.deviceName.choices=([(name,name) for name in data["dicDev"].keys()])
        pass


    def getDict(self):
        mess=dict()
        mess["exe"]="addEffect"
        mess["conName"]=self.conName.data
        mess["effectName"]=self.effectName.data
        mess["deviceName"]=self.deviceName.data
        mess["trueValue"]=self.trueValue.data
        mess["falseValue"]=self.falseValue.data
        return mess

class addSmall(FlaskForm):
    conName = SelectField("conName",validators=[DataRequired()])
    smallName = StringField('smallName', validators=[DataRequired()])
    dev1 = SelectField('dev1', validators=[DataRequired()])
    value1 = IntegerField('Value1',validators=[NumberRange(min=-1, max=255)])
    dev2 = SelectField('dev2', validators=[DataRequired()])
    value2 = StringField('Value2',validators=[NumberRange(min=-1, max=255)])
    cond=SelectField('cond', validators=[DataRequired()])
    submit = SubmitField('Save')

    def setChoices(self,data):
        self.conName.choices=[(name,name) for name in data["dicCon"].keys()]
        self.dev1.choices=[("Value","Value")]+([(name,name) for name in data["dicDev"].keys()])
        self.dev2.choices=[("Value","Value")]+([(name,name) for name in data["dicDev"].keys()])
        self.cond.choices=[(name,name) for name in data["possibleCond"]]
        pass

    def getDict(self):
        mess=dict()
        mess["exe"]="addSmall"
        mess["conName"]=self.conName.data
        mess["smallName"]=self.smallName.data
        mess["dev1"]=self.dev1.data
        mess["value1"]=self.value1.data
        mess["dev2"]=self.dev2.data
        mess["value2"]=self.value2.data
        mess["comp"]=self.cond.data
        return mess