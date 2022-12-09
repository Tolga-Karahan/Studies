## Tasks are Functions
	Prefect tasks are functions that have rules about when they should run. 
	
## Workflows are containers
	Workflows are containers for tasks and they define the dependencies between tasks but don't perform any logic.
	
## Communication via state
	Both workflows and tasks have states that reflect the behaviour at any time.
	
## Prefect Task Scheduling
	Prefect flows themselves handle scheduling of its tasks. It takes burden off the central scheduler.
	Flow and Task runners are responsible of updating database regarding flow, task states on the contrary of Airflow in which scheduler handles database updates.
	
## RunConfig
    There are different types of RunConfigs which configures the flows regarding how they run and where they run. Each type of RunConfig has a corresponding agent. For example flows that are deployed as k8s jobs can be reconfigured by passing a KubernetesRun to run_config parameter of the flow.