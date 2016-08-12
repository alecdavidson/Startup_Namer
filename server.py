import flask, flask.views, os, main

app = flask.Flask(__name__)

app.secret_key = "CorrectTurtleBatteryStaple"

class View(flask.views.MethodView):
  def get(self):
    return flask.render_template('index.html')
  
  def post(self):
    main.main()
    return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])


