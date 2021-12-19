from graph import*

f=lambda x,A,B: A/np.sin((x-B)*np.pi/360)**4
#f=lambda x,A,B: A/np.sin((x-B)/2)**4

loc="pr.xls"

n=1
m=2

bbox=dict(facecolor='white', edgecolor='black', boxstyle='round',alpha=0.5)
bounds=((2e-3,1),(7e-3,1))

print(loc)
data= excel_file(loc, 1)
#print_file("gold_5mm.txt",[1,5])
pov,povc=curve_fit(f,data[m],data[n],method='dogbox')#,bounds=bounds)

par_names=["A","B"]

chi2,DOF,par_err = other_params(f,data[m],data[n],pov,povc,names=par_names)

text= "A = %0.3e +/- %0.3e\n"%(pov[0],par_err[0])+"B = %0.3e +/- %0.3e"%(pov[1],par_err[1])

plt.semilogy(data[m],data[n],"r*",ls='',label="Data")

x=np.linspace(-30,-5,100)
y=np.linspace(5,30,100)



text= "A = %0.3e +/- %0.3e\n"%(pov[0],par_err[0])+"B = %0.3e +/- %0.3e"%(pov[1],par_err[1])
plt.semilogy(x,f(x,*pov),color="green",label="Fit")
plt.semilogy(y,f(y,*pov),color="green")

plt.legend(title=text,shadow=True,ncol=2,loc="best")#.set_draggable(True)
plt.xlabel(r"$\theta$ in degree")
plt.ylabel(r"$N(\theta)$")
plt.title("GOLD FOIL 5mm")
#plt.text(7.5,4,text,bbox=bbox)

plt.grid()


plt.show()
#plt.savefig("gold_5mm.png")

