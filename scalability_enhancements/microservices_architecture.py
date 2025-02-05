import os
from fastapi import FastAPI
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from docker import from_env

app = FastAPI()

# Docker client
docker_client = from_env()

# Kubernetes configuration
config.load_kube_config()

@app.post("/deploy_microservice")
def deploy_microservice(image: str, name: str, replicas: int):
    try:
        # Create a Kubernetes API client
        api_instance = client.AppsV1Api()

        # Define the deployment
        deployment = client.V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=client.V1ObjectMeta(name=name),
            spec=client.V1DeploymentSpec(
                replicas=replicas,
                selector={"matchLabels": {"app": name}},
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(labels={"app": name}),
                    spec=client.V1PodSpec(
                        containers=[
                            client.V1Container(
                                name=name,
                                image=image,
                                ports=[client.V1ContainerPort(container_port=80)],
                            )
                        ]
                    ),
                ),
            ),
        )

        # Create the deployment
        api_instance.create_namespaced_deployment(
            namespace="default", body=deployment
        )
        return {"message": "Microservice deployed successfully"}
    except ApiException as e:
        return {"error": f"Exception when calling AppsV1Api->create_namespaced_deployment: {e}"}

@app.post("/build_image")
def build_image(dockerfile_path: str, tag: str):
    try:
        # Build the Docker image
        image, logs = docker_client.images.build(path=dockerfile_path, tag=tag)
        return {"message": "Docker image built successfully", "image_id": image.id}
    except Exception as e:
        return {"error": f"Exception when building Docker image: {e}"}
