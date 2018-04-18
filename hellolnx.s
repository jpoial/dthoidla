// tekstifail: hellolnx.s
// assembleri n2ide Linuxi keskkonnas "Tere, maailm!"
// Kompileerida ja linkida nii:
// as -o hellolnx.o hellolnx.s && ld -s -o hellolnx hellolnx.o
// Binaarkuju vaatamiseks: hexdump -C hellolnx
// Disassembler: objdump -D hellolnx

.section .text			# koodisektsioon
	.globl	_start		# sisendpunkt - informatsioon linkeri jaoks
_start: movl	$4,%eax		# 4 on "write" katkestuse 0x80 jaoks
	xorl	%ebx,%ebx
	incl	%ebx		# 1 on stdout
	movl	$s6ne,%ecx	# s6ne algusaadress
	movl	$pikkus,%edx	# s6ne pikkus
	int	$0x80		# call "write", parameetriteks %eax, %ebx, %ecx, %edx (, %esi, %edi)
	xorl	%eax,%eax
	incl	%eax		# 1 on "exit"
	xorl	%ebx,%ebx	# 0 on l6petuskood
	int	$0x80 		# call "exit", parameetriteks %eax, %ebx
	hlt			# siia ei j6uta kunagi (hlt igaks juhuks)
.section .data			# andmesektsioon
s6ne:	.string "Tere, digitarkuse omandaja!\012"
pikkus = .-s6ne			# kahe aadressi vahe annab pikkuse
// faili l6pp

