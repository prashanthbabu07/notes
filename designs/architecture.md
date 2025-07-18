# Reason for using MediatR


Why
1. Are we going have any event handler with in-app. if not and all of the events/messages will be sent via azure service bus and event grid then we need to rethink the benifit of using mediatr.
2. Are we planning for request logging. We can still use dotnet middleware for this task?
3. The semantic validations can be perfomred via the validators and explictly called in services.
4. While we want make the code easier to read having a service class will end-up handling many behaviours and become hard to maintain.
5. If we are utilizing other micro-services for notifications etc then publishing events from the server method are okay we don't need mediatr
6. Are we okay to have service classes depend on other services classes?
7. 

@Derek Wade @Eric D. Boyd

The reasoning behind using MediatR or similar pattern was to -

Separation of request, validators and handlers.
Not rely on external systems for publishing events and used in-process notification handling and use NotficationService calls for sending alerts by listening to events.
For Logging, validations via pipeline.
Avoid Service class that can grow large and becomes hard to maintain example IClientService e.g.

Since we are utilizing Azure services and -

If we plan to utilize azure service bus, event grid then we may not need mediatr as it will add more indirection.
If we plan to utilize built-in middleware for logging (define) then we may not need mediatr.
If we plan to utilize fluent validation and are okay to call explicitly in the service methods then we may not need mediatr.
If the service class become too complex and gets too large, we we plan to have a feature based service class we may not need mediatr. i.e. IClientService vs IClientRegistrationService or ?
If we have service-to-service dependency should we have conductor/orchestrator that takes both dependency then work with those service classes or ?
   IClientRegistrationService depends on IClientContactService.
As we are planning for high percentage of test coverage having handler means writing more code. 



