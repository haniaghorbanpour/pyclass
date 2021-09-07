adad = list()
start=1
total=0
while start>=0:
    start=int(input("adaddet ro vared kon:)"))
    if start>= 0:
       adad.append(start)
    elif start<0:
            for ele in range(0, len(adad)):
                total = total + adad[ele]
            print(adad)
            print(total)
            print(total/len(adad))
            break
