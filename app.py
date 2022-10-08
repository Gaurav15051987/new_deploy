import json

import flask
from flask import Flask, jsonify, request, render_template
import pandas as pd
import pickle

df_final = pickle.load(open("song_data_new.pkl", "rb"))
json_without_slash = pickle.load(open("json_without_slash.pkl", "rb"))


# print(final_popular_df)

app = Flask(__name__)

@app.route('/')
def main_page():
        # json_without_slash
    final_json=json_without_slash
    return jsonify(final_json)


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_song', methods=['post'])
def recommend():
    # item = []
    # global book_json
    # input_dict = json.loads(json_without_slash)
    user_input = request.form.get('user_input')
    print(user_input)
    # output_dict = [x for x in input_dict if x['title_request'] == user_input]
    output_dict = df_final[df_final['title_request'] == user_input].to_dict("records")
    # print(index)

    output_json = json.dumps(output_dict)
    return output_json


#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0',port=8050)