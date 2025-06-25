API - Application programmign interface
    This is for source code.

example -
    printf function in c
    

ABI - Application binary interface
    This is for the binary.

example -
    We need to use assembly code for this.  i.e. library sample.


struct {
    int x;
    int y;
} point;

int square(point *p) {
    return p->x * p->x;
}

ASM -

square:
    push ebp
    mov ebp, esp ; Set up stack frame
    mov eax, [ebp+8]  ; Load pointer to point structure
    mov eax, [eax]    ; Load x value
    imul eax, eax     ; Square x value
    pop ebp
    ret

if there is a change in the structure of point, then the assembly code will break.
struct {
    int z;
    int y;
    int y; // New field added
} point;

This is a breakign change in the ABI because the layout of the structure had changed.

To fix we need recompile the user code with the library code.

To avoid compatibility issues the solutions is to use version number in the functions.

i.e. 
int square@v1(point *p) {
    return p->x * p->x;
}

or change the function name
int square_v1(point *p) {
    return p->x * p->x;
}

Who can break the ABI?
- Library developers. 
- Compiler developers.
- Operating system developers.
- Hardware developers.


