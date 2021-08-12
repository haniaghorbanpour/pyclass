def masahat(length , width , measure):
    if measure=="cm":
        length=length/100
        width=width/100
        masahat=length*width
        return masahat
    elif measure=="mm":
        length=length/1000
        width=width/1000
        masahat=length*width
        return masahat
    else:
        length=length
        width=width
        masahat=length*width
        return masahat


m=masahat(float(input("enter length: ")),float(input("enter width: ")),input("enter measure: "))
print(m)
