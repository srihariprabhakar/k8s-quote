## Prerequisites

- A DigitalOcean account with payment set up
- Command Line access with the following installed: kubectl, doctl, git


## Cluster Setup

A DOKS cluster can be setup in one of two ways, steps for which are detailed below:

*DigitalOcean Portal Setup*

1. Sign in to the DigitalOcean portal -> select “Create” on the top right corner -> select Kubernetes.
2. Create a cluster with the following specifications (or based on requirement):

- Kubernetes version: the recommended version, usually the latest stable
- Configure region: datacenter closest to users 
- Size pod and service networks as needed (stick to the “recommended” if unsure)
- Cluster capacity: Basic, s-2vcpu-4gb,set nodepool to autoscale
- Node count: min 2, max 3
- Name the cluster and select a Project
- Click “Create Kubernetes Cluster”


*Command Line Setup*

On a terminal, run the following command and authenticate to DigitalOcean CLI:

            doctl auth init

Create a cluster with the following specifications (or based on requirement):

           doctl kubernetes cluster create cluster-name \
           --region sfo2 \
           --size s-2vcpu-4gb \
           --node-pool "name=default;auto-scale=true;min-nodes=2;max-nodes=3" \
           --version 1.33.1-do.0

Connect kubectl to the cluster and verify:
 
           doctl kubernetes cluster kubeconfig save cluster-name
           Kubectl get nodes


## Application deployment

Once the cluster is created, the containerized application can be set up by cloning the GitHub repo and applying all the required manifests.

1. Clone the GitHub repo on the cluster and switch to the app directory:

           git clone https://github.com/srihariprabhakar/k8s-quote.git
           cd k8-quote

2. Create a namespace to deploy the application into:

           kubectl create namespace webapp

3. Apply all of the manifests (deployments to spin up application pods, service to point traffic to the relevant pods via the LoadBalancer, and the hpa to enable pod autoscaling)

          kubectl apply -f k8s/deployment.yaml -n webapp
          kubectl apply -f k8s/service.yaml -n webapp
          kubectl apply -f k8s/hpa.yaml -n webapp

5. Enable the metrics server for the hpa to autoscale:

        kubectl apply -f     https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

Get the external IP of the service to access the application:

           kubectl get svc -n webapp
