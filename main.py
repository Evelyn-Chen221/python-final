#使用者輸入年所得
total_income=int(input('請輸入您的年所得：'))
#計算需要繳的總稅
if(total_income<=520000) :
	tax_money=total_income*0.05
	print("您總共需要繳{tax_money}元")
elif(total_income>=520001 and total_income<=1220000) :
	tax_money=520000*0.05+(total_income-520000)*0.12
	print("您總共需要繳{tax_money}元")
elif(total_income>=1220001 and total_income<=1920000):
	tax_money=520000*0.05+(1220000-520000)*0.12+(total_income-1220000)*0.2
	print("您總共需要繳{tax_money}元")
elif(total_income>=1920001 and total_income<=2620000): 
	tax_money=520000*0.05+(1220000-520000)*0.12+(1920000-1220000)*0.2+(total_income-1920000)*0.3
	print("您總共需要繳{tax_money}元")
else:
	tax_money=520000*0.05+(1220000-520000)*0.12+(1920000-1220000)*0.2+(2620000-1920000)*0.3+(total_income-2620000)*0.4
	print("您總共需要繳{tax_money}元")
		