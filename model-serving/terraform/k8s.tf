resource "kubernetes_namespace" "prediction-service" {
  metadata {
    name = "prediction-service"
  }
}

resource "null_resource" "load-image" {

 provisioner "local-exec" {

    command = "minikube image load adjoe-task:0.1.0"
  }
}

resource "kubernetes_deployment" "prediction-service" {
    depends_on = [ kubernetes_namespace.prediction-service, null_resource.load-image ]
    metadata {
        name = "prediction-service"
        labels = {
            app   = "prediction-service"
        } //labels
        namespace = "prediction-service"
    } //metadata
    
    spec {
        selector {
            match_labels = {
                app   = "prediction-service"
            } //match_labels
        } //selector
        #Number of replicas
        replicas = 1
        #Template for the creation of the pod
        template { 
            metadata {
                labels = {
                    app   = "prediction-service"
                } //labels
            } //metadata
            spec {
                container {
                    image = "adjoe-task:0.1.0"   #Docker image name
                    name  = "prediction-service"          #Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL).
                    
                    #List of ports to expose from the container.
                    port { 
                        container_port = 8080
                    }//port          
                    
                    resources {
                        limits = {
                            memory = "1Gi"
                        } //limits
                        requests = {
                            cpu    = "250m"
                            memory = "128Mi"
                        } //requests
                    } //resources
                } //container
            } //spec
        } //template
    } //spec
} //resource
#-------------------------------------------------
# KUBERNETES DEPLOYMENT PREDICTION SERVICE SVC
#-------------------------------------------------
resource "kubernetes_service" "prediction-service-svc" {
    depends_on = [ kubernetes_deployment.prediction-service ]
  metadata {
    name = "prediction-service-svc"
    namespace = "prediction-service"
  } //metadata
  spec {
    selector = {
      app = "prediction-service"
    } //selector
    port {
      port      = 8000
    } //port
    type = "ClusterIP"
  } //spec
} //resource