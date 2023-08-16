from flask import Flask,request,render_template,jsonify
from scr.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            Total_Stops=float(request.form.get('Total_Stops')),
            Day = int(request.form.get('Day')),
            Month = int(request.form.get('Month')),
            Year = int(request.form.get('Year')),
            Dept_Hour = int(request.form.get('Dept_Hour')),
            Dept_Min = int(request.form.get('Dept_Min')),
            Arrival_min = int(request.form.get('Arrival_min')),
            Arrival_hour = int(request.form.get('Arrival_hour')),
            duration_hour = int(request.form.get('duration_hour')),
            duration_min = int(request.form.get('duration_min')),
            Source = request.form.get('Source'),
            Airline= request.form.get('Airline'),
            Destination = request.form.get('Destination'),
            dditional_Info = request.form.get('dditional_Info')
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)