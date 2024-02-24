## Auto Scaling Group
- Scales out to match the increasing load or scales in to remove redundant instances.
- Minimum, maximum and desired number of instances can be defined.
- Scoped to multi-AZ setup in the same region.
- Re-creates an EC2 instance in case it is unhealthy.
- For free. Only instances are charged.
- Can work with load-balancers.
- A launch template is used to control scaling.
- CloudWatch alarms can be used for scaling.

## Scaling Policies
- Dynamic Policies:
    - Target Tracking Scaling:
        - Works by setting a rule for example average ASG CPU should stay at %40.
    - Simple/Step Scaling:
        - Works based on triggered CloudWatch alarms. 
        - Step Scaling takes an action based on the defined rule and action.
        - Step Scaling can have multiple steps. For example if CPU usage is more than %80, add 2 instances, or if it is less than %30 remove 1 instance etc.
    - Scheduled Actions:
        - Anticipating a surge in a period. For example increase the min capacity to 10 on Fridays, or during a predefined time of event etc.
    - Predictive Scaling:
        - Based on forecasting the load and scheduling ahead.

## Scaling Cooldowns
- The period in which no instance launched/terminated after a scaling activity.
