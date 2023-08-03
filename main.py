import websocket
import _thread
import time
import rel
import tinytuya
import json
import datetime
from dotenv import load_env
load_env()

people = 0

bulb1 = tinytuya.BulbDevice(os.environ['BULB1_ID'], os.environ['BULB1_IP'], os.environ['BULB1_KEY'])
bulb2 = tinytuya.BulbDevice(os.environ['BULB2_ID'], os.environ['BULB2_IP'], os.environ['BULB2_KEY'])

bulb1.set_version(3.3)
bulb2.set_version(3.3)


def on_message(ws, message):
	if datetime.datetime.now().hour < 19: print("not 7pm yet"); return
	global people
	message = json.loads(message)
	print(message)
	if "msg" in message:
		if "gesture" in message['msg']:
			gesture = int(message['msg']['gesture'])
			out = 4
			in_ = 3
			if gesture == out: people -= 1
			if gesture == in_: people += 1
			if people < 0: people = 0
			if people == 0: bulb1.turn_off(); bulb2.turn_off(); print("lights off")
			if people > 0: bulb1.turn_on(); bulb2.turn_on(); print("lights on")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    ws.send(os.environ["NODE_KEY"])

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://193.122.164.255:8080/v1/node/event",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=9999999999999999999999)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
