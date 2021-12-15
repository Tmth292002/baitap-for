def xulychuoi():
    string = "{}, {}, {}".format("Greek", "for", "life")
    print("Xu li chuoi1: ", string)

    string1 = "{1}, {2}, {0}".format("Greek", "for", "life")
    print("Xu li chuoi2: ", string1)

    string2 = "{f}, {k}, {l}".format(f = "Greek",l = "for",k =  "life")
    print("Xu li chuoi3: ", string2)

if __name__ == "__main__":
    xulychuoi()