# Counter with Python and Flask
This repo contains simple app to detect IP Address and count the hit number of visitor.

### Details

The app is written in Python, using Flask framework 

 - `app.py` is the actual app code
 - `requirements.txt` are the dependencies required to run the app
 - `Dockerfile` is used to build docker container
 
 ### Building/testing steps

Download/pull this repository:
`git clone https://github.com/anwareset/dockerquestion.git`

Go to the newly created directory
`cd hit-counter`

Build and tag your docker image

`docker build -t hit-counter . `

Make sure to push the image to docker hub:
`docker push trianwar/hit-counter`

You can test your application and its dependency (Redis) using docker-compose.
`docker-compose up -d --build`

### Deployment steps
We can deploy to the Kubernetes cluster:
 
#### 1. Manually creating pods
```shell
cd kubernetes
kubectl apply -f pods_service.yml 
```

#### Cleanup
To do some cleanup, run the following commands:
`kubectl delete all`

#### 2. Using a _Deployment_ controller
```shell
cd k8s
kubectl create -f deployments.yml 
kubectl create -f services.yml 
```
 
#### Cleanup
To do some cleanup, run the following commands:
```shell
kubectl delete deployment app-deployment
kubectl delete deployment redis-depoyment
kubectl delete all
```

### Scale Up
Adjust the N number
`kubectl scale app-deployment deployment --replicas=N`
Or simply use the HPA.
