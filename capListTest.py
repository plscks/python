def all_casings(input_string):
    if not input_string:
        yield ""
    else:
        first = input_string[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(input_string[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(input_string[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing

ext = []
jpg = [x for x in all_casings('.jpg')]
png = [x for x in all_casings('.png')]
ext.extend(png)
ext.extend(jpg)
truth = '.jpg' in ext
print(truth)
print(ext)
