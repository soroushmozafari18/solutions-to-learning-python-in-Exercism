def label(colors):
    color_list=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    num_1=color_list.index(colors[0])
    num_2=color_list.index(colors[1])
    num_3=color_list.index(colors[2])
    if num_1==0:
        num_1=''
    number=int(str(num_1)+str(num_2)+(str(0)*(num_3)))
    if (number%(10**3))==0:
        if number%(10**6)==0:
            if number%(10**9)==0:
                return '0 ohms' if number==0 else str(number)[:-9]+' gigaohms'
            else:
                return str(number)[:-6]+' megaohms'
        else:
            return str(number)[:-3]+' kiloohms'
    else:
        return str(number)+' ohms'

