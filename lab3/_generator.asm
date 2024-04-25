.686
.model flat

.data
	fifty dd 50.0
	hundred dd 100.0
.code

_generator PROC
	push ebp
	mov ebp, esp

	fld dword ptr [ebp+8]
	fld hundred
	fmulp
	
	fld fifty
	faddp

	pop ebp
	ret
_generator ENDP

END