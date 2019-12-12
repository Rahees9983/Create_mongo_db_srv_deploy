import os
# import kubernetes
from os import path

import yaml
import subprocess

from kubernetes import client, config


import time

# from kubernetes import config, client
from kubernetes.client import Configuration
# from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import logging


# s = os.system("mkdir aaaa")
# print(s)
# a = os.system("rmdir aaaa")
# print(a)

minikube_status_var = """host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured"""

# print(minikube_status_var)
# exit(0)
# v = subprocess.getoutput("vboxmanage --version")
# print(type(v))
# print(v)
# vv = os.system("vboxmange --version")
# print("value of vv ",vv)

# namespace1 = os.system("kubectl create namespace namespaec-1")

# namespace2 = os.system("kubectl create namespace namespaec-2")

# namespace3 = os.system("kubectl create namespace namespaec-3")

# logging.info("Oracel virtual Box installed successfully and version is "+str(os.system("vboxmanage --version")))
# os.system("kubectl create namespace mongo-namespace")

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


# create_mongo_delploy()
# create_mongo_service()

s = subprocess.getoutput("kubectl get pods --namespace mongo-namespace | grep mydb")
print(s)