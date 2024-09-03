from flask import Flask, render_template
app=Flask(__name__)
#localhost:500
@app.route('/')
def main():
    return render_template('dasboard.html',page='main')
@app.route('/apex')
def apex():
    return render_template('charts-apexcharts.html',page='login')
@app.route('/das')
def das():
    return render_template('dasboard.html',page='dashboard')
@app.route('/echar')
def echar():
    return render_template('charts-echarts.html',page='charts-echarts')
@app.route('/chartjs')
def chartjs():
    return render_template('charts-chartjs.html',page='chartjs')