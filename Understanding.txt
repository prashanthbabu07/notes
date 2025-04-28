Thread sleep - 
	There is only few clocks in computer and need to utilize the same clock across multiple processes
	The kernel will use a separate queue and can utilize the same CPU clock timer for all of these. 
	Rather than using CPU like a loop the kernel will move this into it's own queue.
	Once the time is elapsed the kernel will move this to ready queue to continue the program.
	
System calls - 
	When we use println! in rust, printf in c this will be a system call to kernel.
	The kernel will has code to change flags in CPU such that the code can run in kernel mode.
	The kernel mode will have higher privileges such that it can work with driver and hardware peripherals. 
	
Context switching - 
	While we have multiple programs/processing all running concurrently feels like all running at the same time.
	This is achieved by switching process in CPU such that everyone program will get some CPU time.
	Currently kernel use preemptive system way to switch between processes i.e. after a scheduled time the process get's switched.
	This preemptive is achieved by the scheduler sending an interrupt such that OS can now do a context switch.
	The kernel can also add software interrupt as well. 
	In a cooperative system the process might take all of the CPU resources and can halt other programs.
	
Async/Await - 
	The async/await works when there a non block io being performed by the process or a program.
	If there a blocking io then the control is not handed back.
	Let's assume a main function that is running in a main thread. 
		The main thread will create a another thread which is a runtime that manages asyns/await tasks.
		If there are a, b, c tasks that has some potential io tasks (non blocking) then the async runtime 
		can give the control back and forth between a, b and c tasks. 
		The code is still running in synchronous but the tasks get's switched whan there a some io work.
	The runtime like dotnet or tokio in rust utilizes OS epoll for checking for any events.
		Take for example when we connect to a socket it will provide a file descriptor (fd number) associated with that socket.
		The fd is then handed over to epoll to check for any events like receiving data through that socket connection.
		The epoll adds to the list of fd that needs to watched.
		Say if the client send some data through the socket then the epoll can check for the even receive event and and hand over 
		control back to the next set of instructions.
		But rather than having a loop to keep checking these fd's in the kernel which is inefficient.
		The kernal will have these fd list and when data starts coming through the socket the nic (network interface card) can raise
		and interrupt such that OS kernel can check for the fd's based on the info coming from nic and wake the fd that is of interest.
		This can then be send runtime such that it can then run the tasks which is just waiting.
		
Threads - 
	Program counter for each entity i.e. threads
	Each thread should have it's own state i.e. CPU registers, program counter, flags, accumulator it's own CPU state.
	

		

		
		
		
		
		
		
		
		
		
		
