from flask import Flask,render_template,request,send_file

#from werkzeug import secure_filenmae

import pandas as pd 

app = Flask(__name__)

# @app.route('/')
# def index():
# 	return render_template('index.html')

@app.route('/success')
def show_file():
	df = pd.read_excel('open_file.xlsx')
	#df = pd.DataFrame(data)
	sum = df['English'] + df['Telugu'] + df['Maths'] + df['Science']
	df['total'] = df['English'] + df['Telugu'] + df['Maths'] + df['Science']
	avg = (df['total'])/4
	df['Percentage %'] = (df['total'])/4

	#df.set_index(['Name','English','Tekugu','Maths','Science','Total','%Percentage'])
	#return render_template('index.html', show = df.to_html())
	return df.to_html()

@app.route('/')
def upload_file():
	return render_template('upload.html')


@app.route('/uploader', methods =["POST"])
def uploader():
	tot_mark = 100
	if request.method == "POST":
		file_upload = request.files['file']
		try :

			print("indside uploader")
			data_xls = pd.read_excel(file_upload)
			#sum = data_xls['Engish'] + data_xls['Telugu'] + data_xls['Maths'] + data_xls['Science']
			#data_xls['total'] = data_xls['Engish'] + data_xls['Telugu'] + data_xls['Maths'] + data_xls['Science']
			sum = data_xls['English'] + data_xls['Telugu'] + data_xls['Maths'] + data_xls['Science']
			print (sum)
			data_xls['total'] = data_xls['English'] + data_xls['Telugu'] + data_xls['Maths'] + data_xls['Science']
			avg = ((data_xls['total']/tot_mark)*100)
			data_xls['% Percentage'] = ((data_xls['total']/tot_mark)*100)
			print("before return")

			grade = []

			for row in data_xls['% Percentage'] :
				if row > 95 :
					grade.append('A+')
				elif row < 95 and row > 80 :
					grade.append('A')
				elif row < 80  and row > 70 :
					grade.append('B+')
				elif row < 70 and row > 60 :
					grade.append('B')
				elif row < 60 and row > 45 :
					grade.append('C')
				else :
					grade.append('Fail / Absent')

			data_xls['grade'] = grade

			return render_template('upload.html',text=data_xls.to_html())
		except Exception as e:
			return render_template('index.html' ,  text=str(e))




# @app.route("/Upload", methods=["POST","GET"])
# def upload_file():
#     if request.method == 'POST':
#         print(request.files['file'])
#         f = request.files['file']
#         data_xls = pd.read_csv(f)
#         sum = data_xls['Engish'] + data_xls['Telugu'] + data_xls['Maths'] + data_xls['Science']
#         data_xls['total'] = data_xls['Engish'] + data_xls['Telugu'] + data_xls['Maths'] + data_xls['Science']

#     #return render_template('upload.html',text=data_xls.to_html())

# @app.route("/export")
# def export_records():
#     return send_file(file)










if __name__ == '__main__':
	app.run(debug = True)