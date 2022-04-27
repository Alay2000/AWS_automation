# AWS_automation

## Project Name 
AWS S3 and Ec2 using boto3 and flask

## To run and test

  1) Install docker and pull the image from docker hub using
  
  --> sudo docker pull alayinnogeeks/aws:v4
 
  2) Run the container passing the AWS credentials access key and secret key as environment variables and map the port 5000. the command is shown below
  
  -->sudo docker run --name <name the container> -p 5000:5000 -e AWS_ACCESS_KEY_ID=<aws access key id from iam> -e AWS_SECRET_ACCESS_KEY=<your secret access key from iam> -e AWS_DEFAULT_REGION=us-east-1 alayinnogeeks/aws:v4
  
  3)Can be hosted on amazon EC2 be connecting the instance through ssh and following the steps 1 and 2 on terminal
  
## Usage
  
  Can be used to easily create and manage amazon Ec2 instances and S3 buckets from a single web application of a particular user
  
## Contributing
  
  One can raise issues and make merge requests for adding more AWS functionalities such as IAM, Database, and much more.
  One can convert the HTML CSS to a react application
  
## Tech Stack Used
  
   used flask for routing and python as backend. 
   Boto3 is used for making connections, passing data to AWS in the backend
   Simple HTML, CSS and Bootstrap is used for frontend for testing later to be converted to a react application
 
  
  
