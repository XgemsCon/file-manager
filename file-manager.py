"""
         Author : Adnan Khan 
         email  : Adnankhan526252@gmail.com
"""


from flask import * 

app = Flask(__name__)

#main route
@app.route("/")
def index():
	return render_template('app.html')

if __name__=="__main__":
	app.run(debug=True)