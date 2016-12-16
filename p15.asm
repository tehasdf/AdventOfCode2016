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
    mov r8, 1  ; t
    mov rax, 0
    l1:  ; iterate over t
        mov rcx, startpos  ; iterator over startpos
        mov r9, discs  ; end boundary for startpos
        mov r11, discs  ; iterator over discs
        l2:  ; iterate over startpos and discs
            movzx rax, byte [rcx]  ; compute (t + startpos[i]) % discs[i]
            add rax, r8
            movzx r15, byte [r11]
            xor rdx, rdx
            div r15
            cmp rdx, 0
            jne nonzero  ; if any of them is nonzero, continue to the next t

            inc r11
            inc rcx

            cmp rcx, r9
            jne l2  ; next disc
        jmp success  ; all discs checked and we didnt jmp to nonzero - all are 0

        nonzero:
            inc r8
            jmp l1

    success:
        mov rdi, print_int
        mov rsi, r8
        mov rax, 0
        call printf
