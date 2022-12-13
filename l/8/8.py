def stringsum():
    while True:
        num=input("Enter numbers only.")
        if num.isdigit():
            break
        print('Enter only numbers.\n')
    total=0
    for n in num:
        total+=int(n)
    print(f"The total is {total}.")
def date():
    date_form='11/11/1111'
    while True:
        forma=''
        date=input("Enter a date.")
        for l in date:
            if l.isdigit():
                forma+='1'
            elif l=='/':
                forma+='/'
        if forma==date_form:
            break
        print("Enter a proper date format.\n")
    months=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    num=date[:2]
    month=months[int(num)]
    print(f"The date is {month} {date[3:5]}, {date[6:]}")
def morsecode():
    letter=['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--',
              '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••']
    nums=['•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•', '-----']
    abc='abcdefghijklmnopqrstuvwxyz'
    numbers='123456789'
    msg2=''
    while True:
        j=0
        msg=input("Enter a message.").lower()
        msg8=msg.split()
        for hn in msg8:
            if not hn.isalnum():
                j=1
        if j==0:
            break
        else:
            print("Enter only letters and numbers.")
    for thi in msg:
        if thi.isalpha():
            c=abc.index(thi)
            c=letter[c]
            msg2+=c
        elif thi.isdigit():
            c=numbers.index(thi)
            c=nums[c]
            msg2+=c
        elif thi==' ':
            msg2+=' / '
    print(msg2)
def phone_convert():
    phone=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],
           ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    pho_format='xxx-xxx-xxxx'
    while True:
        pnum=''
        forma=input("Enter a phone #.").lower()
        for thi in forma:
            if thi.isalnum():
                pnum+='x'
            elif thi=='-':
                pnum+='-'
            else:
                pnum+='65'
        if pnum==pho_format:
            break
        print("Enter a good format.")
    new_num=''
    for thi in forma:
        if thi.isalpha():
            for lists in phone:
                if thi in lists:
                    new_num+=str(phone.index(lists)+2)
        elif thi.isdigit():
            new_num+=thi
        else:
            new_num+=thi
    print(f"The new number is {new_num}")
def avgwords():
    file=open('text.txt','r')
    everything=''
    cou=0
    for line in file:
        line.replace('\n',' ')
        everything+=line
    sente=everything.count('.')
    everything=everything.split()
    for thi in everything:
        cou+=1
    avg=cou/sente
    print(f"There are {cou} words")
    print(f"There are {sente} sentences.")
    print(f"The average number of words is {avg}")
def piglatin():
    sente=input("Enter a msg to be changed.").upper()
    sente=sente.split()
    sente2=''
    for word in sente:
        new_word=word[1:]+word[0]+"AY"
        sente2+=new_word+' '
    print(sente2)
def pblott():
    freq,lotto_numbers=pbfreq()
    freq_sort=[]
    for e in freq:
        freq_sort.append(e)
    freq_sort.sort()
    freqs=[]
    for loop in range(0,2):
        freq_sort.reverse()
        for jk in range(0,9+1):
            current_freq=freq_sort[jk]
            position=freq.index(current_freq)
            freq[position]=-1
            currently_occuring_number=lotto_numbers[position]
            freqs.append(currently_occuring_number)
    freq_sort.reverse()
    print('most occurring')
    for jk in range(0,9+1):
        print(freqs[jk],'occuring ',freq_sort[jk])
    freq_sort.reverse()
    print('least occurring')
    for jk in range(10,19+1):
        print(freqs[jk],'occuring ',freq_sort[jk-10])
def pbfreq():
    pbmbers=open('pbnumbers.txt', 'r')
    contents=''
    for line in pbmbers:
        contents=contents + line[:15]
    contents=contents.split()
    lotto_numbers=['01','02','03','04','05','06','07','08','09']
    for num in range(10,69+1):
        lotto_numbers.append(str(num))
    freq=[]
    for num in lotto_numbers:
        freq_count=contents.count(num)
        freq.append(freq_count)
    return freq,lotto_numbers
def gp():
    average_prices, lowps, higps = gpi()
    year = 1993
    for price in average_prices:
        print(f'gas priced in {year} was {price}')
        year += 1
    print()
    for msg in lowps:
        print(msg)
    print()
    for msg in higps:
        print(msg)
def gpi():
    file=open('GasPrices.txt', 'r')
    gasprices_in_years=[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']] #WILL BE SORTED
    gasprices_unsorted=['']
    lth=['']
    htl=['']
    dates_unsorted=['']
    current_year=1993
    year=0
    line=file.readline()
    while line!='':
        if line[6:9+1]==str(current_year):
            gasprices_in_years[year][0]+=line[11:].replace('\n',' ')
            dates_unsorted[0]+=line[:10+1].replace(':',' ')
            gasprices_unsorted[0]+=line[11:].replace('\n',' ')
            lth[0]+=line[11:].replace('\n',' ')
            htl[0]+=line[11:].replace('\n',' ')
            line=file.readline()
        else:
            current_year+=1 
            year+=1
    file.close()
    year=0
    for prices in gasprices_in_years:
        gasprices_in_years[year][0]=gasprices_in_years[year][0].split()
        year+=1
    dates_unsorted=dates_unsorted[0].split()
    gasprices_unsorted=gasprices_unsorted[0].split()
    lth=lth[0].split()
    htl=htl[0].split()
    average_gasprices_in_years=[]
    year=0
    gas_price=0
    total=0
    while year<21:
        try:
            total+= float(gasprices_in_years[year][0][gas_price])
            gas_price+=1
        except:
            average=total/gas_price
            average_gasprices_in_years.append(format(average,'.2f'))
            year+=1
            gas_price=0
            total=0
            average=0
    higps=[]
    lowps=[]
    current_year=1993
    for year in range(0,21):
        high_price=max(gasprices_in_years[year][0])
        low_price=min(gasprices_in_years[year][0])
        higps.append(high_price)
        lowps.append(low_price)
        higps[year]=f'highest gas in {current_year} was '+higps[year]
        lowps[year]=f'lowest gas in {current_year} was '+lowps[year]
        current_year+=1
    file=open('lowtohigh.txt', 'w')
    lowtohigps=['']
    lth.sort()
    for price in lth:
        price_index=gasprices_unsorted.index(price)
        date=dates_unsorted[price_index]
        lowtohigps[0]+=f'{date}:{price} '
    lowtohigps=lowtohigps[0].split()
    for line in lowtohigps:
        file.write(line + '\n')
    file.close()
    file=open('highttolow.txt', 'w')
    higtolowps=['']
    htl.sort()
    htl.reverse()
    for price in htl:
        price_index = gasprices_unsorted.index(price)
        date = dates_unsorted[price_index]
        higtolowps[0]+=f'{date}:{price} '
    higtolowps=higtolowps[0].split()
    for line in higtolowps:
        file.write(line+'\n')
    file.close()
    return average_gasprices_in_years, lowps, higps