## Tasks are Functions
	Prefect tasks are functions that have rules about when they should run. 
	
## Workflows are containers
	Workflows are containers for tasks and they define the dependencies between tasks but don't perform any
    logic.
	
## Communication via state
	Both workflows and tasks have states that reflect the behaviour at any time.
	
## Prefect Task Scheduling
	Prefect flows themselves handle scheduling of its tasks. It takes burden off the central scheduler which
    only creates future flow runs. Flow and Task runners are responsible of updating database regarding flow,
    task states on the contrary of Airflow in which scheduler handles database updates. 

## Flow Configuration
    1 - Storage
            Storage objects define in where a flow is stored such as local, S3, Docker etc. Only a reference
        to storage is keep by Prefect backend. It has no direct access to the code. For example Docker storage
        puts flows inside a Docker image and pushes them to a container registry.
	
    2 - Run Configuration
            RunConfig objects configures the flows regarding how they run and where they run. There are different
        types of RunConfigs. Each type of RunConfig has a corresponding agent. For example flows that are deployed
        as k8s jobs can be reconfigured by passing a KubernetesRun to run_config parameter of the flow.

            Labels can be added to RunConfig objects. Only agents whose labels are superset of the RunConfig of the
        flow can run those flows.

    3 - Executor
            An executor is responsible for running tasks of a Flow.
## Agents
    1 - Kubernetes Agent
            Kubernetes agent deploys flows as k8s jobs. It uses either a UniversalRun or KubernetesRun object.
        KubernetesRun object is used to configure deployment environment.  

## Reliability
    Lazarus process retries flow runs that are running but have no running or submitted tasks. Most common situation
    is pod is not spinned, or pod is gone before run is completed.

    Zombie Killer process queries tasks that in running state, but don't update their heartbeat in the past 2 minutes
    for Prefect Cloud and 5 minutes for Prefect Server. This tasks are marked as failed by Zombie Killer.