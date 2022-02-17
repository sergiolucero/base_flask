from flask import Flask

psum = lambda p: sum(pow(ix, -p) for ix in range(1,1000000))

app = Flask(__name__)

@app.route('/psum/<p>')
def home(p):
    ps = round(psum(int(p)))
    return {"hello": ps}
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
