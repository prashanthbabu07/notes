# dotnet 

Create new solution
dotnet new sln -n MySolution -- where MySolution is the name of the solution

Create new class library project
dotnet new classlib -n MyLibrary -- where MyLibrary is the name of the class library

Create new test project
dotnet new xunit -n MyTests -- where MyTests is the name of the test project

Create new console application project
dotnet new console -n MyApp -- where MyApp is the name of the console application

Create new web api project
dotnet new webapi -n MyWebApi -- where MyWebApi is the name of the web API project

Create new mvc web application project
dotnet new mvc -n MyMvcApp -- where MyMvcApp is the name of the MVC web application

Add existing project to solution
dotnet sln MySolution.sln add MyLibrary/MyLibrary.csproj

Add dependencies local project
dotnet add MyApp/MyApp.csproj reference MyLibrary/MyLibrary.csproj

Add NuGet package to project
dotnet add MyApp/MyApp.csproj package Newtonsoft.Json --version 13.0.1 

List NuGet package installed in project
dotnet list MyApp/MyApp.csproj package

List NuGet package available versions
dotnet list MyApp/MyApp.csproj package --outdated

Restore NuGet packages for project
dotnet restore MyApp/MyApp.csproj

Build solution
dotnet build MySolution.sln

Build specific project
dotnet build MyApp/MyApp.csproj

Run project
dotnet run --project MyApp/MyApp.csproj

Publish project
dotnet publish MyApp/MyApp.csproj -c Release -o ./publish

Run tests in project
dotnet test MyTests/MyTests.csproj

List test projects in solution
dotnet test --list

Run specific test in a test project
dotnet test MyTests/MyTests.csproj --filter "FullyQualifiedName~MyNamespace.MyTestClass.MyTestMethod"


