from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def fetch_data(bikeid="", shopname="", userid="", brandname=""):
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = 'bikes'
    )
    cursor = mydb.cursor()
    # get all the employee details
    if len(bikeid)>1:
        query = """
                select b.*,s.*, r.*

                from bikes.bikes as b

                inner join bikes.shops as s
                on b.bikeid = s.bikeid and b.bikeid={id}
    
                inner join bikes.rents as r
                on r.hrs = s.hrs and s.bikeid = {id};

                """
        
        
        cursor.execute(query.format(id=int(bikeid)))
        sequence = cursor.column_names
        query_result = tuple()
        for res in cursor:
            query_result=query_result+res
        return(sequence, query_result)
        



@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        bikeid = request.form['bikeid']
        shopname = request.form['shopname']
        userid = request.form['userid']
        brandname = request.form['brandname']
        sequence, result = fetch_data(bikeid, shopname, userid, brandname)
        return render_template("result.html", headings=sequence, data=result)
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
    