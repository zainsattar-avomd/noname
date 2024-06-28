### React, PostgreSQL, and Cloud Services Integration Challenge (Thought Exercise)

Design a system architecture for a scalable, real-time chat application using React for the frontend, PostgreSQL for database management, and AWS or Azure for cloud services. Your design should include:

User authentication and data security measures.
Real-time message exchange and storage strategies.
Scalability solutions for growing numbers of users and messages.
Integration of a feature that allows users to send cryptocurrency tips to each other, leveraging blockchain technology.

Provide a detailed discussion on how you would approach user authentication, data security, real-time communication, and the integration of blockchain technology for the tipping feature. Include considerations for choosing specific AWS or Azure services to support these functionalities.


### Approach

Refer to Image in the folder.

1. AWS Amplify : deployment service for the client app. provides cdn configurations for fast delivery of
html/javascript all around the world. uses s3 buckets for cheap storage. provides integrated CI/CD pipeline
for deployments. Also has Backend as a service which will be used to write secure apis, with high availability
and other features for communicating with the server.

2. React app with websockets: I have decided to use react for the front-end of the client app. We will be using 
web sockets for the chat feature. This will allow us to do real-time message exchange with multiple other users
and can be scaled to a resonable amount. React has multiple javascript packages that can be used for crypto currency
tipping featues

3. Route53: routing and domain settings for our webserver

4. Api Gateway: provides a way for creating websockets, Apis and rerouting to various services such a aws incognito,
lamda functions and your own server

5. AWS Cognito (optional): We can use this for authentication and authorizations. Cognito provides us with secure identity store, which is scalable and uses secure token based protocols (Oauth 2, openid) for maximum security during authentication. You can use this to login via google,facebook etc, create complex identity and user pools for
select authorization, and provides good analytics which are essential for chat apps. However, this can be skipped
and you can use your custom servers for this purpose as well

6. Load Balancer and ec2 instance managed by elastic beanstalk:  This is our main application server. Where our
app logic/business logic resides. We use loadbalancers for high thoroughput and availability. Elastic Beanstalk
allows us to dynamically scale vertically or horizontally by selecting EC2 instance sizes and scaling from 1 to n
instances during peak loads. For security, we will make sure we have CORS settings enabled, using a framework like
node or django which protects from dependency injections and Man in the middle attacks etc.

7. Redis/ElasticCache: This will help the application scale and improve speed. You can keep encrypted chats in the
Cache to reduce hits on the database and to provide real-time communications

8. RDS Postgres: RDS is a fully managed service which can help with dynamic scaling, High consistency and availabilty and security by providing multi-az deployments, secure backups etc

9. S3 buckets: used for media files for our chat apps

10. Lambda(optional): you can have seperate lambda services that can handle crypto exchange if required. You can 
also skip this and add the logic to your server. However, these allow you run any language seperate from your main server and removes dependency and load on your main server for speedy payments. We Can use any thirdparty service for
crypto transactions
