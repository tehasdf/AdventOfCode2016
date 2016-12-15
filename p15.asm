; nasm -felf64 p15.asm && gcc p15.o && ./a.out

global main
extern printf

section .data
startpos:
    db 5+1, 8+2, 1+3, 7+4, 1+5, 0+6, 0+7
discs:
    db 17, 19, 7, 13, 5, 3, 11
print_int:
    db "%d", 10, 0

section .text
main:
    mov r8, 1

    l1:
        mov rcx, startpos
        mov r11, discs
        mov r9, discs
        l2:
            movzx rax, byte [rcx]
            add rax, r8
            movzx r15, byte [r11]
            xor rdx, rdx
            div r15
            cmp rdx, 0
            jne nonzero

            inc r11
            inc rcx

            cmp rcx, r9
            jne l2
        jmp success

        nonzero:
        inc r8
        jmp l1

    success:
        mov rdi, print_int
        mov rsi, r8
        mov rax, 0
        call printf
