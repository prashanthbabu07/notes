When working on coding with team or alone there is one thing we need to always think about i.e.

1. How do I make sure that a feature or code that is already working need not be touched 
again for adding new feature unless there is a bug or issue to fix.

2. How to have certain guidelines or reasoning that can be set so everyone in the team can follow and apply.
    What does this mean it's answered and questioned below since we need a consistent way to handle exceptions
    and how each classes i.e. caller and called methods communicate. The reasoning here is that a consistent 
    way to strcutre the code helps other team members to read/update code as if they have written.

3. Where to write what code. This is something I always think about.
    This is important since having a clear set of principals makes it easier for long term projects.
    The code in controllers are only suppose to enhance the request and then pass it on the the chain of request handlers.
    The code in each pipeline should do what the class name states. i.e. ExceptionCatcher, RequestLogger, RequestSemanticValidator etc.

4. Who is responsbile for managing exceptions/errors.
    The core idea is who introducted the exceptions/error should take responsiblity of managing it.
    i.e. say we create a table called Client and create a ClientRepository that can work wtih client table.
    The repository knows a lot about the table than any other high level classes or modules.
    If there are any exceptions i.e. genuine whcih the repository could not fulfill then will end up up exceptions.
    Say we introduce a constrain like unique key on client name then this rule can throw exception by the base 
    class but they are not exceptions instead they are part of the business logic to have a unique values in that column 
    so that needs to be treated differently and handled differently in the system. The ideal way to manage them is irrespective
    of the underlying implemention if it throws exceptions the repository is supposed to catch and then transform then
    into error's and return with correct Result not throw exceptions and some higher level module handle them.


5. Until you can explain the problem in simple engligh it's hard to write code for the same. So having 
to say it loud helps.

Here's what I think should happen.

The classes should be deep i.e. it's okay to have any number of methods that will alway mutate it's internal state.

Always works with an understanding that you'll not have complete details upfront. So solve for the current given 
problem and then extend based of future info.
What does it mean?
    Initially we had a requirement to timeline where users wanted to add message to timeline. We said that is easy
let's create class that will perform this action.

e.g. in C# but the same can be applied for others.

inteface ITimeLineService {
    void AddMessage(string message);
}

class TimeLineService : ITimeLineService {
    List<string> messages;

    void AddMessage(string message) {
        messages.Add(message);
    }
}

After pushing this feature the users like the app and started asking for edit message feature :( 
We can add a new specification to the interface as below but we are making chagnes to something that's already existing,
also doing this we need to implement the same in TimeLineService and any other classes that uses them.
inteface ITimeLineService {
    void AddMessage(string message);
    void EditMessage(string message);
}

We need something better so we don't do this and either we need to have extend add capabilities without making changes to
existing class code. 

The interface or specification needs to be clean up to support.

We need to create interfaces using the capability i.e.

interface IAddMessage {I {Capability:Add} {Type: Message})
interface IEditMessage ...

We use language features to implement them. 

partial class TimeLineService 
{
    TimeLineService() {
    }
}

partial class TimeLineService : IAddMessage {
}

partial class TimeLineService : IEditMessage {
}

and so on... this design makes the class extend without touching existing code and add capabilities without affecting others.

This enables other developers to add capabilitites without worrying about other dev's adding their own capability.

The interfaces should be specific such that the implementer can take what they are able to implement.


