from flask import Flask, jsonify
import crawler
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import db_functions
app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(func=crawler.save_current_occupancy, trigger="interval", minutes=10)
scheduler.start()


@app.route("/")
def hello():
    return jsonify(db_functions.get_all_entries())

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())