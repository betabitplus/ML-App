Create a docker image:

      $ docker image build -t ml-app .

Run container:

      $ docker run -p 5001:5000 -d ml-app

Open in the browser:

      http://localhost:5001/

The app looks like the following.

![alt text](https://i.ibb.co/Jd6CcW0/app-1.jpg)

Once the document was chosen press the 'Classify the document!' button.

![alt text](https://i.ibb.co/Wzrd6H6/app-2.jpg)

The result will be similar to this.

![alt text](https://i.ibb.co/2KBYF8M/app-3.jpg)