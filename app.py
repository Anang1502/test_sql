import os
import time
import config as cf
import datetime
from src.utils.sql_db.get_from_db import FetchData
from flasgger import Swagger, swag_from
from flask import Flask, request, jsonify, send_from_directory


app = Flask(__name__)
app.debug = True
app.url_map.strict_slashes = False
app.secret_key = 'production'

Swagger(app)

@app.route("/", methods=['GET', 'OPTIONS'])
def hello():
    """Main route to check if the server is online"""
    return jsonify({"Result": {"message": "Hello from SIMPLIFAI.AI NLU:DocumentBot"}})


@swag_from(os.path.join(cf.BASE_PATH, "api_doc", "get_details.yml"))
@app.route("/api/v1/get_details", methods=["POST", "OPTIONS"])
def get_details():
    try:
        table_dict = []
        start_date = request.form["StartDate"]
        bot_id = request.form["BotID"]
        if "EndDate" not in request.form:
            end_date = str(datetime.date.today())
        else:
            try:
                end_date = request.form["EndDate"]
                datetime.datetime.strptime(start_date, "%Y-%m-%d")
                datetime.datetime.strptime(end_date, "%Y-%m-%d")
                if time.strptime(start_date, "%Y-%m-%d") > time.strptime(end_date, "%Y-%m-%d"):
                    return jsonify(
                        {"Result": {"Msg": "start_date should be before or same as end_date."}})
            except ValueError:
                return jsonify({"Result": {"Msg": "This is the incorrect date string format. It should be YYYY-MM-DD"}})
        fetch_obj = FetchData(bot_id, start_date, end_date)
        details = fetch_obj.main()
        for row in details:
            table_dict.append({"date": row[0], "bot_id": row[1], "bot_name": row[2], "docs_processed": row[3],
                               "pages_processed": row[4]})
        return jsonify({"Result": {"data": table_dict}})
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(host='localhost', port=5017)