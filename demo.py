from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, make_response
import time

app = Flask(__name__)

def slow_query():
  time.sleep(10)
  return "Slow query executed at " \
      + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
  
@app.route('/quick')
def quick_query():
  time.sleep(0.1)
  response = make_response("Quick query executed at " \
      + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
  response.headers['Cache-Control'] = 'max-age=0'
  return response

@app.route('/')
def show_front_page():
  response = make_response( \
      render_template('front_page.html', slow_query=slow_query(), quick_query=quick_query()))
  response.headers['Cache-Control'] = 'max-age=0'
  return response

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
