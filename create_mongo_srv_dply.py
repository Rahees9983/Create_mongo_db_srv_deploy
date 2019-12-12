from os import path
import os
import yaml
import subprocess

from kubernetes import client, config
import time

# creating mongo-namespace namespace 
os.system("kubectl create namespace mongo-namespace")

def create_mongo_delploy():
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "mydb_deploy.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="mongo-namespace")
        print("Deployment created. status='%s'" % resp.metadata.name)

def create_mongo_service():
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "mydb_service.yaml")) as f:
            dep = yaml.safe_load(f)
            k8s_apps_v1 = client.CoreV1Api()
            # resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
            resp = k8s_apps_v1.create_namespaced_service(namespace="mongo-namespace", body=dep)
            print("Deployment created. status='%s'" % resp.metadata.name)


create_mongo_delploy()
create_mongo_service()