    It's a deployment strategy to put software into production as smooth as possible. To do that
    two different but identical environments are used. They are called blue and green environment. 
    At any time one of them is live. 

    When there is a new release, software is tested, for example, on green environment and if it
    works, routes configured so that incoming requests go to the green environment. Blue is now
    idle. 

    It also allows us to rollback to previous release by switching routes to blue environment in 
    case something goes wrong. If new release works well in green environment then blue environment
    is used as a staging environment for final testing of next deployment. For the next release, 
    routes are switched to blue environment as it is done for the previous release from blue to
    green. In that way both environments are regularly cycling between live, previous version(for
    rollback) and staging the next version. 