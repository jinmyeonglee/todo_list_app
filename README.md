# Simple todo app
To understand Verda.
### You should add config file(ini) after cloning.
```ini
[MySQL]
port =
host =
name =
user =
pwd =

[VOS]
access_key =
secret_key = 
s3_host =
bucket_name =

[Redis]
host =
port =
pwd =
```
### If you want to servive using VKS, you shold add these 2 files.
1. openrc file to check auth which can be downloaded in Verda.
2. password file in which you should write down your Connect password.

#### And then use these commands.
```shell script
kubectl create -f namespace.yaml

kubectl create -f deployment.yaml

kubectl create -f ingress.yaml -n ingress-nginx
```
