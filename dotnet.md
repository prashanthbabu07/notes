# dotnet 

When installing dotnet we need sdk for development and runtime needed for running the app.

There are 2 runtimes base runtime and asp runtime

base runtime is used for running console apps
asp runtime is needed for running asp web apps

-------

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

## Testing

-- report generator
dotnet tool install -g dotnet-reportgenerator-globaltool

--install coverlet (coverlet is a cross-platform code coverage framework for .NET)
dotnet tool install -g coverlet.console

-- test using code converage settings
dotnet test --settings CodeCoverage.runsettings --collect:"Code Coverage"

--XPlat Code Coverage (XPlat Code Coverage is a cross-platform code coverage tool for .NET Core)
dotnet test --collect:"XPlat Code Coverage"

-- run tests with coverlet
dotnet test MyTests/MyTests.csproj --collect:"XPlat Code Coverage" -- DataCollectionRunSettings.DataCollectors.Configuration.Format=cobertura
-- run tests with coverlet and output to cobertura format

dotnet test MyTests/MyTests.csproj --collect:"XPlat Code Coverage" -- DataCollectionRunSettings.DataCollectors.Configuration.Format=cobertura -- DataCollectionRunSettings.DataCollectors.Configuration.OutputDirectory=./TestResults

-- report generator
reportgenerator -reports:./TestResults/coverage.cobertura.xml -targetdir:./CodeCoverageReport -reporttypes:Html
