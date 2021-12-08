# Counter with Python and Flask
This repo contains simple app to detect IP Address and count the hit number of visitor.

### Details

The app is written in Python, using Flask framework 

 - `app.py` is the actual app code
 - `requirements.txt` are the dependencies required to run the app
 - `Dockerfile` is used to build docker container
 
 ### Building/testing steps

Download/pull this repository:
```shell
git clone https://github.com/anwareset/dockerquestion.git
```

Go to the newly created directory
```shell
cd hit-counter
docker build -t hit-counter .
docker tag hit-counter trianwar/hit-counter
docker-compose up -d --build
```

### Deployment steps
We can deploy to the Kubernetes cluster
 
#### 1. Manually creating pods
```shell
cd kubernetes
kubectl apply -f pods_service.yml 
```

#### Cleanup
To do some cleanup, run the following commands:
```shell
kubectl delete all
```

#### 2. Using a _Deployment_ controller
```shell
cd kubernetes
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
```shell
kubectl scale app-deployment deployment --replicas=N
```
Or simply use the HPA.
