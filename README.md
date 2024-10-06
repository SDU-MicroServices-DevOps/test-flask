# README
Simple Flask project to test and showcase github actions with GKE.

Current implementation is not suited for production usage. Please change the underlying webserver in production.

# Github Actions
Github Actions file is based on the Google starter workflow (https://github.com/actions/starter-workflows/blob/main/deployments/google.yml)

Required environment variables:
* Project id
* Google Artifact Registry Location
* GKE cluster
* GKE Zone
* Deployment name
* GAR Repository name
* Image name
* Workload Identity Provider
   * can be found by
```bash
gcloud iam workload-identity-pools providers describe github-actions-provider \
  --location=global \
  --workload-identity-pool="my-app-dev-pool"
```

Required files in the repository:
1. Dockerfile -> Description of the container, used to built the Image
2. deployment.yaml -> Description of the deployment settings in the kubernetes cluster
3. service.yaml -> Description of the service settings in the cluster

Optional files in the repository:
1. kustomization.yaml -> Used for renaming references

# Google Cloud
- Create GKE cluster.
   - The kubernetes cluster used in this test is created with only default settings. 
   - The type of cluster used is Autopilot.

- Create Google Artifact Registry Repository.

- Blogpost explaining how to create and use WIF.
   * https://cloud.google.com/blog/products/identity-security/enabling-keyless-authentication-from-github-actions

- Create Service account:
   * Roles:
     * Artifact Registry Administrator
     * Kubernetes Engine Cluster Viewer
     * Kubernetes Engine Developer
     * Workload Identity User
- Workload Federation Identity Pool and Provider
   * attribute.repository_owner="SDU-MicroServices-DevOps" (attribute conditions) 
   * or 
   * assertion.repository=='SDU-MicroServices-DevOps/test-flask'
