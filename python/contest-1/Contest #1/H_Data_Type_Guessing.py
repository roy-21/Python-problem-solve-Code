#input
n,k,a=map(int, input().split())

#new_variable_er_modhe_n_k_a_gun kore_rakhbo

result=n*k*a

#check_conditions

if -2^31 <= result <= 2^31-1:
    print("int")
else:
    print("long long")
