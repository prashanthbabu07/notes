When working on coding with team or alone there is one thing we need to always think about i.e.

1. How do I make sure that a feature or code that is already working need not be touched 
again for adding new feature unless there is a bug or issue to fix.

2. How to have certain guidelines or rules that can be set so everyone in the team can follow and apply.

3. Where to write what code. This is something I always think about.

4. Who is responsbile for managing exceptions/errors.

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


