# Code by @AmirMotefaker

# With the help of @jadijadi

# معمای ریاضیاتی پیدا کردن رمز گاوصندوق

# سینا پین کد ۵ رقمی گاوصندوق خود را فراموش کرده است. با این حال، اطلاعاتی درباره اعداد پین کد خود دارد:
# – جمع رقم های پنجم و سوم پین کد برابر با چهارده است.
# – رقم اول، یک واحد از دوبرابر رقم دوم کمتر است.
# – رقم چهارم، یک واحد از رقم دوم بیشتر است.
# – جمع رقم های دوم و سوم برابر با ده است.
# – حاصل جمع رقم های پین کد برابر با ۳۰ است.

# با توجه به این اطلاعات، پین کد سینا را تعیین کنید.


def jame_argham(ramz_digits):
    sum_digits = 0
    for k in ramz_digits:
        sum_digits += ramz_digits[k]
    return sum_digits

def ramz_is_ok(ramz_digits):
    if ramz_digits['panj'] + ramz_digits['se'] == 14 and \
        ramz_digits['yek'] == ramz_digits['do']* 2 - 1 and \
        ramz_digits['chahar'] == ramz_digits['do'] + 1 and \
        ramz_digits['do'] + ramz_digits['se'] == 10:
            if jame_argham(ramz_digits) == 30:
                return True
    #return True
for ramz in range(0, 100000): # chon bayad 5 raghami bashe ta hadeaksar 99999 javab mideh
    this_ramz = str(ramz).zfill(5)

    ramz_digits = {} # moarefi Dictionary ramz_digits
    ramz_digits['yek'] = int(this_ramz[0])
    ramz_digits['do'] = int(this_ramz[1])
    ramz_digits['se'] = int(this_ramz[2])
    ramz_digits['chahar'] = int(this_ramz[3])
    ramz_digits['panj'] = int(this_ramz[4])
    #print(ramz)
    if ramz_is_ok(ramz_digits):
       print(ramz)
