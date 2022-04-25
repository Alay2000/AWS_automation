from crypt import methods
from flask import Flask, render_template, request
import aws_bucket, aws_ec2, os

app=Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "alay"


@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/createbucket')
def add():
    return render_template('add.html',var='createbucket')



@app.route('/createbucket/success', methods=['POST'])
def function1():
    if request.method=='POST':
        bucket_name=request.form['name']
        location=request.form['Location']
    return aws_bucket.createbucket(bucket_name, location)


@app.route('/listallbuckets')
def function2():
    return aws_bucket.listallbuckets()


@app.route('/getbucketpolicy')
def add1():
    return render_template('add.html',var='getbucketpolicy')

@app.route('/getbucketpolicy/success',methods=['POST'])
def function3():
    if request.method=='POST':
        bucket_name=request.form['name']
    return aws_bucket.getbucketpolicy(bucket_name)


@app.route('/creationtime')
def function4():
    return aws_bucket.creationTime()

@app.route('/deletebucketpolicy')
def add2():
    return render_template('add.html',var='deletebucketpolicy')


@app.route('/deletebucketpolicy/success',methods=['POST'])
def function5():
    if request.method=='POST':
        bucket_name=request.form['name']
    return aws_bucket.deletebucketpolicy(bucket_name)

@app.route('/uploadfile')
def functionupload():
    return render_template('add.html',var='upload')

@app.route('/uploadfile/success', methods=['POST'])
def function6():
    f = request.files['file']
    f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    return aws_bucket.uploadfile(f"uploads/{f.filename}", "alay")
    


@app.route('/downloadfile')
def function7():
    return aws_bucket.downloadfile()


@app.route('/createinstance')
def functioncreate():
    return render_template('ec2add.html',var="create")

@app.route('/createinstance/success', methods=['POST'])
def function8():
    keyname=request.form['name']
    return aws_ec2.create_instance(keyname)

@app.route('/getrunninginstances')
def function9():
    return aws_ec2.get_running_instances()

@app.route('/stopinstance')
def function10():
    return render_template('ec2add.html',var='stopinstance')

@app.route('/stopinstance/success', methods=['POST'])
def function11():
    name=request.form['name']
    return aws_ec2.stop_instance(name)

@app.route('/getpublicip')
def function12():
    return render_template('ec2add.html',var='getpublicip')

@app.route('/getpublicip/success',methods=['POST'])
def function13():
    name=request.form['name']
    return aws_ec2.get_public_ip(name)

@app.route('/terminate_instance')
def function14():
    return render_template('ec2add.html',var='terminate')

@app.route('/terminateinstance/success',methods=['POST'])
def function15():
    name=request.form['name']
    return aws_ec2.terminate_instance(name)

@app.route('/rebootinstance')
def function16():
    return render_template('ec2add.html',var='reboot')

@app.route('/reboot/success',methods=['POST'])
def function17():
    name=request.form['name']
    return aws_ec2.reboot_instance(name)

@app.route('/describeinstance')
def function18():
    return render_template('ec2add.html',var='describe')

@app.route('/describe/success',methods=['POST'])
def function19():
    name=request.form['name']
    return aws_ec2.describe_instance(name)



if __name__=='__main__':
    app.run(debug=True)