from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class AddValue(FlaskForm):
    name=StringField('name', validators=[DataRequired()])
    value=StringField('value',validators=[DataRequired()])
    submit = SubmitField('Save')
    def getDict(self):
        mess=dict()
        mess["exe"]="addValue"
        mess["name"]=self.name.data
        mess["value"]=self.value.data
        return mess


class addDevice(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    desc = StringField('desc', validators=[DataRequired()])
    typeName = StringField('IP Address', validators=[DataRequired()])
    refreshTime = IntegerField('refreshTime',validators=[DataRequired()])
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

    def PreWrite(self,device):
        self.name.default=device["name"]
        self.name.render_kw={"readonly":True}
    
        self.desc.default=device["desc"]
        
        self.typeName.default=device["typeName"]
        self.refreshTime.default=device["refreshTime"]
        self.isRec.default=device["isRec"]
        
        #self.process()
        
    

class addCon(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    desc = StringField('desc', validators=[DataRequired()])
    refreshTime = IntegerField('refreshTime',validators=[DataRequired()])
    submit = SubmitField('Save')

    def getDict(self):
        mess=dict()
        mess["exe"]="addCon"
        mess["name"]=self.name.data
        mess["refreshTime"]=self.refreshTime.data
        mess["desc"]=self.desc.data
        print(mess)
        print("wwwww")
        return mess

class addEffect(FlaskForm):
    conName = SelectField("conName",validators=[DataRequired()])
    effectName = StringField('effectName', validators=[DataRequired()])
    deviceName =  SelectField('deviceName', validators=[DataRequired()])
    trueValue = StringField('trueValue',validators=[DataRequired()])
    falseValue = StringField('falseValue',validators=[DataRequired()])
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
    value1 = StringField('Value1',validators=[DataRequired()])
    dev2 = SelectField('dev2', validators=[DataRequired()])
    value2 =StringField('Value2',validators=[DataRequired()])
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
