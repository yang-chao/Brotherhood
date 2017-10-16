from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/archived')
def archived():
    apkPath = 'static'
    filePaths = os.listdir(apkPath)
    launchName = ''
    testName = ''
    preName = ''
    for path in filePaths:
        if not os.path.isdir(path):
            basename = os.path.basename(path)
            if 'Launch' in basename:
                launchName = basename
            elif 'Test' in basename:
                testName = basename
            elif 'Pre' in basename:
                preName = basename
    return render_template('archived.html', launchName=launchName, testName=testName, preName=preName)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')