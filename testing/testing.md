# Testing


Unit testing - 

"Unit" key for testing, ability to methods in a class in isolation. 

Ability to test the class behaviour but we can have n number of methods ideally unit test should 
focus on methods in classes.
    
Say we have a Repository class that has a dependency on database you can't unit test since?

But say we have some rule i.e. no duplicate email address then the code need to go and check in db 
depending on the outcome the process may insert record or not. 

For to test this rule we are dependent on Repositoy class say PersonRepository. But we can't unit test
having a db dependency so we need a mock the PersonRepository i.e. create an interface that can be easily
switched with mock repository and perform unit testing for email address exists.

The catch is that interface might have many declaration i.e. AddPerson, DeletePerson, EmailExists. The mock has
to implemente all of them. So we need a better interface design i.e.

ICanAddPerson, ICanDeletePerson, ICanCheckEmailExists this does help for mocking and testing features I like this
way of thinking but what are the downsides? tiny interfaces.

Why You Mock user_exists
To test business logic, validation, or service layer code without involving the real database.

Interface segregation principal (ISP) is about client perspective and not implementors.

What does it mean -
A Person registration needs -
Email Exists
Add Person 

A Admin panel needs
Add Person
Delete Person
Edit Person
Email Exists

Having a tiny interface is much better than a fat interface. Take this example using C as example with header file.
// person_repository.h

#ifndef PERSON_REPOSITORY_H
#define PERSON_REPOSITORY_H

#include <stdbool.h>

// --- ICanAddPerson Interface ---
void add_person(const char* name, const char* email);

// --- ICanDeletePerson Interface ---
void delete_person(int id);

// --- ICanCheckEmailExists Interface ---
bool email_exists(const char* email);

// --- ICanGetPerson Interface ---
Person* get_person_by_id(int id);
Person** get_all_persons(int* count);

#endif
